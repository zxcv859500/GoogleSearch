import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import pyPdf
import io
import re
import threading

#TODO http://dgkim5360.tistory.com/entry/python-pdfminer-convert-pdf-to-html-txt

def Extractor(path, filename, keyword, line):
    file = path + '\\' + filename
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

    sover = ''
    res = []
    for text in data:
        sover = sover +str(text)
    sover = sover.replace('\t', ' ')
    sover = sover.replace('\n\n', '\n')

    texts = sover.split('\n')
    number = texts.__len__()

    passnum = 0
    for idx in range(number):
        if passnum != 0:
            passnum -= 1
            continue

        temp = ''
        if keyword in texts[idx]:
            print(texts[idx])
            for idx2 in range(idx, idx + line):
                temp += texts[idx2]
                passnum = line
            res.append(temp)


    return res

def GetFileList(path):

    file_list = os.listdir(path)

    return file_list

def mktext(path, filename, data):

    with open(path+'\\'+filename+'.txt', 'w', encoding='UTF-8') as f:
        for line in data:
            f.write(line + '\n')

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

def OpenFile(path, filename):

    os.system(path + '\\' + filename)

if __name__ == '__main__':
    #Extractor('C:\\Users\\조나단\\Desktop\\Test\\KLC_대회규정.pdf', '퍼즈')
    #GetCleanFileList('C:\\Users\\조나단\\Desktop\\Test')
    data = Extractor('C:\\Users\\조나단\\Desktop\\Test\\', '하이브리드롤_기반_대면적_핫엠보싱_장비.pdf',
                     '고기능화', 2)
    mktext('C:\\Users\\조나단\\Desktop\\Test\\', '하이브리드롤_기반_대면적_핫엠보싱_장비'
           , data)