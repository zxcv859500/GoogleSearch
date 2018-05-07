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

def GetFileList(path):

    file_list = os.listdir(path)

    return file_list

def mktext(path, filename, data):

    with open(path+'\\'+filename+'.txt', 'w') as f:
        for line in data:
            f.write(line)

def DeleteExcept(filename):

    exname = filename.split(r"\\")[-1].split('.')[-1]

    if exname != 'pdf' and exname != 'PDF' and exname != 'txt':
        os.remove(filename)
        print(filename.split(r'\\')[-1] + ' delete complete')

def DeleteFile(path, filename):

    filepath = path + '\\' + filename

    os.remove(filepath)

def GetCleanFileList(path):

    file_list = os.listdir(path)

    for file in file_list:

        DeleteExcept(path + '\\' + file)

if __name__ == '__main__':
    #Extractor('C:\\Users\\조나단\\Desktop\\Test\\KLC_대회규정.pdf', '퍼즈')
    GetCleanFileList('C:\\Users\\조나단\\Desktop\\Test')