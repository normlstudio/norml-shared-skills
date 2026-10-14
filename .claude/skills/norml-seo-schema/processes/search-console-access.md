# Optional Search Console access

URL Inspection API reports Google's indexed URL information, not a live test or
an indexing request. Recent deploys may not yet be reflected. Always record the
last crawl and compare it with your deployment evidence.

## Dependencies and authentication

Python 3 plus `google-auth`, `google-api-python-client`, and supported ADC from the
user's authorized Google identity. Use the user's existing provider connection or
Google-supported OAuth/ADC flow with `webmasters.readonly` scope. Installation and
provider-login actions follow the user's environment policies; secrets never go
in chat, source, task reports or shared archives. ADC may be provider-managed;
otherwise use the operating system protected credential store. Do not create a
company-specific cloud project, impose a fixed quota project or claim service
accounts are universally unsupported. Property authorization must actually pass.

## Run

```bash
python3 scripts/gsc-inspect.py --site sc-domain:example.com https://example.com/page/
python3 scripts/gsc-inspect.py --json https://example.com/page/
```

Without --site the helper lists the authorized properties and selects the longest
matching URL prefix or matching Domain property. An explicit --site still must be
in that identity's authorized inventory and cover every requested URL. Missing or
ambiguous property access blocks inspection and leaves local validation available.
Requests are sequential. API quota/rate errors are reported without retries or
provider mutation. --raw prints inspection content only, not credentials.

[API method and scopes](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect)
[Search Console authorization](https://developers.google.com/webmaster-tools/v1/how-tos/authorizing)
