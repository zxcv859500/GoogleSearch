import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

def Extractor(file, keyword):

    fp = open(file, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

    texts = str(data)
    print(texts)
    print(texts.split('.'))

    res = []

    for text in texts.split('.'):
        if keyword in text:
            res.append(text)
            print(text)

    return res

def mktext(filename, data):

    pass

def DeleteExcept(filename):

    exname = filename.split(r"\\")[-1].split('.')[-1]

    print(exname)

    if exname != 'pdf':
       os.remove(filename)

if __name__ == '__main__':
    #Extractor('C:\\Users\\조나단\\Desktop\\Test\\KLC_대회규정.pdf', '퍼즈')
    DeleteExcept('C:\\Users\\조나단\\Desktop\\Test\\ac_downFile.asp')