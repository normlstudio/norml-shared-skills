"""Build native Docs requests with UTF-16 indices and explicit tab selection."""
def utf16_length(text):
    return len(text.encode('utf-16-le'))//2

class DocBuilder:
    def __init__(self, start=1, tab_id=None):
        if start < 1: raise ValueError('Body starts at index 1')
        self.reqs=[]
        self.i=start
        self.tab_id=tab_id
    def _range(self,a,b):
        result={'startIndex':a,'endIndex':b}
        if self.tab_id: result['tabId']=self.tab_id
        return result
    def text(self,text,style='NORMAL_TEXT'):
        loc={'index':self.i}
        if self.tab_id: loc['tabId']=self.tab_id
        self.reqs.append({'insertText':{'location':loc,'text':text}})
        a=self.i;self.i+=utf16_length(text)
        if style and self.i>a:
            self.reqs.append({'updateParagraphStyle':{
                'range':self._range(a,self.i),
                'paragraphStyle':{'namedStyleType':style},'fields':'namedStyleType'}})
        return a,self.i
    def heading(self,text,level=1):
        if not 1<=level<=6: raise ValueError('Heading level must be 1..6')
        return self.text(text,f'HEADING_{level}')
    def link(self,a,b,url):
        self.reqs.append({'updateTextStyle':{'range':self._range(a,b),
            'textStyle':{'link':{'url':url}},'fields':'link'}})
