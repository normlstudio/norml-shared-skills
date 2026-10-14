#!/usr/bin/env python3
"""Inspect authorized indexed URLs using the user's provider-supported ADC.

No fixed cloud/quota project. Requires google-auth and google-api-python-client.
See processes/search-console-access.md; this is not a live test or indexing request.
"""
import argparse
import json
import sys
from urllib.parse import urlparse

SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly'

def covers(site, url):
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https') or not parsed.hostname:
        return False
    if site.startswith('sc-domain:'):
        domain = site[10:].lower()
        host = parsed.hostname.lower()
        return host == domain or host.endswith('.' + domain)
    target = urlparse(site)
    return (parsed.scheme, parsed.netloc) == (target.scheme, target.netloc) and parsed.path.startswith(target.path or '/')

def summary(raw):
    result = raw.get('inspectionResult', {})
    indexed = result.get('indexStatusResult', {})
    rich = result.get('richResultsResult', {})
    return {
        'verdict': indexed.get('verdict'),
        'coverage_state': indexed.get('coverageState'),
        'last_crawl': indexed.get('lastCrawlTime'),
        'google_canonical': indexed.get('googleCanonical'),
        'user_canonical': indexed.get('userCanonical'),
        'rich_results_verdict': rich.get('verdict'),
        'rich_results': rich.get('detectedItems', []),
        'evidence_scope': 'Google indexed version; not a live test',
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('urls', nargs='+')
    parser.add_argument('--site', help='Exact authorized URL-prefix or sc-domain: property')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--raw', action='store_true', help='Inspection data only; excludes credentials')
    args = parser.parse_args()
    try:
        import google.auth
        from googleapiclient.discovery import build
        credentials, _ = google.auth.default(scopes=[SCOPE])
        service = build('searchconsole', 'v1', credentials=credentials, cache_discovery=False)
        inventory = service.sites().list().execute().get('siteEntry', [])
    except ImportError:
        print('Missing google-auth/google-api-python-client. Install in your approved Python environment.', file=sys.stderr)
        return 2
    except Exception:
        print('Google identity/authorized property inventory unavailable. Verify the provider connection and readonly scope.', file=sys.stderr)
        return 2
    properties = [entry['siteUrl'] for entry in inventory
                  if entry.get('permissionLevel') != 'siteUnverifiedUser' and entry.get('siteUrl')]
    report, failed = {}, False
    for url in args.urls:
        candidates = [site for site in properties if covers(site, url)]
        if args.site:
            site = args.site if args.site in candidates else None
        else:
            prefixes = [site for site in candidates if not site.startswith('sc-domain:')]
            # Most specific URL-prefix first; fall back to most specific domain.
            ordered = sorted(prefixes or candidates, key=len, reverse=True)
            site = ordered[0] if ordered else None
        if not site:
            report[url] = {'error': 'No matching authorized property; verify --site and resource access.'}
            failed = True
            continue
        try:
            raw = service.urlInspection().index().inspect(body={
                'inspectionUrl': url, 'siteUrl': site, 'languageCode': 'en-US'}).execute()
        except Exception:
            report[url] = {'site': site, 'error': 'Inspection API failed; check permission, scope, quota or provider status.'}
            failed = True
            continue
        result = summary(raw)
        rich_errors = any(issue.get('severity') == 'ERROR'
                          for group in result['rich_results']
                          for item in group.get('items', [])
                          for issue in item.get('issues', []))
        if result['verdict'] != 'PASS' or rich_errors:
            failed = True
        report[url] = {'site': site, **(raw if args.raw else result)}
    if args.json or args.raw:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for url, result in report.items():
            print(url)
            print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if failed else 0

if __name__ == '__main__':
    sys.exit(main())
