"""Exact native Docs selection and revision-guarded update helpers."""

def flatten_tabs(document):
    result = []
    def walk(tabs):
        for tab in tabs:
            result.append(tab)
            walk(tab.get('childTabs', []))
    walk(document.get('tabs', []))
    return result

def select_tab(document, *, tab_id=None, title=None, parent_id=None):
    if not tab_id and title is None:
        raise ValueError('Supply exact tab ID or an unambiguous title')
    matches = []
    for tab in flatten_tabs(document):
        prop = tab['tabProperties']
        if tab_id and prop['tabId'] != tab_id:
            continue
        if title is not None and prop.get('title') != title:
            continue
        if parent_id is not None and prop.get('parentTabId', '') != parent_id:
            continue
        matches.append(tab)
    if len(matches) != 1:
        raise ValueError('Tab selection is missing or ambiguous; use its exact ID')
    return matches[0]

def tab_end(tab):
    return tab['documentTab']['body']['content'][-1]['endIndex'] - 1

def inserted_table(tab, insertion_index, rows, columns):
    candidates = [el['table'] for el in tab['documentTab']['body']['content']
        if 'table' in el and insertion_index <= el.get('startIndex', -1) <= insertion_index + 1
        and el['table'].get('rows') == rows and el['table'].get('columns') == columns]
    if len(candidates) != 1:
        raise ValueError('Inserted table cannot be identified uniquely; stop before filling')
    return candidates[0]

def fill_table_requests(table, rows, tab_id):
    if len(rows) != table.get('rows') or any(len(r) != table.get('columns') for r in rows):
        raise ValueError('Content dimensions differ from selected table')
    requests = []
    for r in range(len(rows) - 1, -1, -1):
        for c in range(len(rows[r]) - 1, -1, -1):
            cell = table['tableRows'][r]['tableCells'][c]
            index = cell['content'][0]['startIndex']
            requests.append({'insertText': {'location': {'index': index, 'tabId': tab_id},
                                            'text': str(rows[r][c])}})
    return requests

def update(docs, document_id, revision_id, requests, *, authorized=False):
    if not authorized:
        raise PermissionError('Exact document change must be authorized')
    if not revision_id or not requests:
        raise ValueError('Read revision and build a nonempty plan before updating')
    return docs.documents().batchUpdate(documentId=document_id, body={
        'writeControl': {'requiredRevisionId': revision_id}, 'requests': requests}).execute()
