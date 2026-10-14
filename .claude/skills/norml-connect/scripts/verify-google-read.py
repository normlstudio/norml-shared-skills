#!/usr/bin/env python3
"""Read-only Google identity and exact GSC/GA4/GTM visibility verification."""
import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def get_json(url, token, quota=None):
    headers = {'Authorization': 'Bearer ' + token}
    if quota:
        headers['X-Goog-User-Project'] = quota
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        return json.loads(response.read())


def inventory(url, key, token, quota):
    rows, seen = [], set()
    while True:
        result = get_json(url, token, quota)
        rows.extend(result.get(key, []))
        next_token = result.get('nextPageToken')
        if not next_token:
            return rows
        if next_token in seen:
            raise ValueError('Repeated pagination token')
        seen.add(next_token)
        # Keep the base endpoint stable and replace, rather than accumulate,
        # pagination parameters across pages.
        base = url.split('?')[0]
        url = base + '?' + urlencode({'pageToken': next_token, 'pageSize': 200})


def target_visible(profile, resources, expected):
    if profile == 'gsc':
        return any(row.get('siteUrl') == expected and
                   row.get('permissionLevel') != 'siteUnverifiedUser' for row in resources)
    if profile == 'analytics':
        return any(prop.get('property') == expected for row in resources
                   for prop in row.get('propertySummaries', []))
    return any(row.get('publicId') == expected for row in resources)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profile', choices=['gsc', 'analytics', 'gtm'])
    parser.add_argument('--account', required=True)
    parser.add_argument('--target', required=True)
    parser.add_argument('--quota-project')
    args = parser.parse_args()
    # ADC is provider-managed. Never read/export its files or print a token.
    import google.auth
    from google.auth.transport.requests import Request as GoogleRequest
    creds, _ = google.auth.default(quota_project_id=args.quota_project)
    creds.refresh(GoogleRequest())
    token = creds.token
    identity = get_json('https://www.googleapis.com/oauth2/v2/userinfo', token)
    if identity.get('email', '').casefold() != args.account.casefold():
        raise ValueError('Google identity mismatch')
    if args.profile == 'gsc':
        rows = get_json('https://searchconsole.googleapis.com/webmasters/v3/sites',
                        token, args.quota_project).get('siteEntry', [])
    elif args.profile == 'analytics':
        rows = inventory('https://analyticsadmin.googleapis.com/v1beta/accountSummaries',
                         'accountSummaries', token, args.quota_project)
    else:
        accounts = inventory('https://tagmanager.googleapis.com/tagmanager/v2/accounts',
                             'account', token, args.quota_project)
        rows = []
        for account in accounts:
            path = account.get('path', '')
            # Do not follow provider-returned absolute URLs to another host.
            if not path.startswith('accounts/') or '..' in path or '?' in path:
                raise ValueError('Unexpected GTM resource path')
            rows.extend(inventory('https://tagmanager.googleapis.com/tagmanager/v2/' +
                                  path + '/containers', 'container', token,
                                  args.quota_project))
    visible = target_visible(args.profile, rows, args.target)
    print(json.dumps({'identity_matches': True, 'target_visible': visible,
                      'profile': args.profile}))
    return 0 if visible else 1


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except HTTPError as exc:
        print(json.dumps({'ok': False, 'http_status': exc.code}), file=sys.stderr)
        raise SystemExit(1)
    except Exception as exc:
        print(json.dumps({'ok': False, 'error_type': type(exc).__name__}), file=sys.stderr)
        raise SystemExit(1)
