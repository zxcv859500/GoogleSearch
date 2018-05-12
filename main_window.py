# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Download_Manager import *
import FilePDFManager
import threading
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_page = QtWidgets.QLabel(self.centralwidget)
        self.label_page.setGeometry(QtCore.QRect(10, 10, 56, 20))
        self.label_page.setObjectName("label_page")
        self.lineEdit_page = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_page.setGeometry(QtCore.QRect(70, 10, 30, 20))
        self.lineEdit_page.setObjectName("lineEdit_page")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 56, 20))
        self.label.setObjectName("label")
        self.lineEdit_Search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Search.setGeometry(QtCore.QRect(70, 40, 220, 20))
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 56, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Path.setGeometry(QtCore.QRect(70, 70, 220, 20))
        self.lineEdit_Path.setReadOnly(True)
        self.lineEdit_Path.setObjectName("lineEdit_Path")
        self.toolButton_Path = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_Path.setGeometry(QtCore.QRect(300, 70, 27, 18))
        self.toolButton_Path.setObjectName("toolButton_Path")
        self.pushButton_Search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Search.setGeometry(QtCore.QRect(380, 10, 121, 81))
        self.pushButton_Search.setObjectName("pushButton_Search")
        #self.lineEdit_FileSearch = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_FileSearch.setGeometry(QtCore.QRect(120, 120, 170, 20))
        #self.lineEdit_FileSearch.setObjectName("lineEdit_FileSearch")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 121, 20))
        self.label_3.setObjectName("label_3")
        #self.pushButton_Log
        self.pushButton_Log = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Log.setGeometry(QtCore.QRect(425, 120, 75, 23))
        self.pushButton_Log.setObjectName('pushButton_Log')
        #self.pushButton_Refresh
        self.pushButton_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(345, 120, 75, 23))
        self.pushButton_Refresh.setObjectName('pushButton_Refresh')
        self.label_progress = QtWidgets.QLabel(self.centralwidget)
        self.label_progress.setGeometry(QtCore.QRect(290, 20, 56, 12))
        self.label_progress.setText("")
        self.label_progress.setObjectName("label_progress")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 150, 491, 341))
        self.listView.setObjectName("listView")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 500, 56, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_Extract = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Extract.setGeometry(QtCore.QRect(70, 500, 113, 20))
        self.lineEdit_Extract.setObjectName("lineEdit_Extract")
        #self.label_Extract_Line
        self.label_Extract_Line = QtWidgets.QLabel(self.centralwidget)
        self.label_Extract_Line.setGeometry(QtCore.QRect(10, 530, 121, 20))
        self.label_Extract_Line.setObjectName("label_Extract_Line")
        #self.lineEdit_Extract_Line
        self.lineEdit_Extract_Line = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Extract_Line.setGeometry(QtCore.QRect(70, 530, 113, 20))
        self.lineEdit_Extract_Line.setObjectName("lineEdit_Extract_Line")
        #self.pushButton_ExtractnOpen
        self.pushButton_ExtractnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ExtractnOpen.setGeometry(QtCore.QRect(190, 530, 75, 23))
        self.pushButton_ExtractnOpen.setObjectName("pushButton_ExtractnOpen")
        self.pushButton_Extract = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Extract.setGeometry(QtCore.QRect(190, 500, 75, 23))
        self.pushButton_Extract.setObjectName("pushButton_Extract")
        self.pushButton__Remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__Remove.setGeometry(QtCore.QRect(270, 500, 75, 23))
        self.pushButton__Remove.setObjectName("pushButton__Remove")
        self.pushButton_OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OpenFile.setGeometry(QtCore.QRect(430, 500, 70, 20))
        self.pushButton_OpenFile.setObjectName("pushButton_OpenFile")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 100, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.model = QtWidgets.QDirModel()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.listView.setRootIndex(self.model.index('C:\\Users\\조나단\\Desktop\\Test\\'))
        #
        #later

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GoogleSearch"))
        self.label_page.setText(_translate("MainWindow", "페이지 수 : "))
        self.label.setText(_translate("MainWindow", "검색어"))
        self.label_2.setText(_translate("MainWindow", "파일 위치"))
        self.toolButton_Path.setText(_translate("MainWindow", "..."))
        self.pushButton_Search.setText(_translate("MainWindow", "검색\n""\n""다운로드"))
        self.label_3.setText(_translate("MainWindow", "파일 목록"))
        self.label_4.setText(_translate("MainWindow", "추출"))
        self.pushButton_Extract.setText(_translate("MainWindow", "추출"))
        self.pushButton__Remove.setText(_translate("MainWindow", "삭제"))
        self.pushButton_OpenFile.setText(_translate("MainWindow", "열기"))
        self.label_Extract_Line.setText(_translate("MainWindow", "줄 수"))
        self.pushButton_ExtractnOpen.setText(_translate("MainWindow", "추출 후 열기"))
        self.lineEdit_Extract_Line.setText(_translate("MainWindow", '1'))
        self.pushButton_Log.setText(_translate("MainWindow", "검색 기록"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "새로고침"))

        ######
        #do
        ######
        self.toolButton_Path.clicked.connect(self.filebtn_click)
        self.pushButton_Search.clicked.connect(self.searchbtn_click)
        self.pushButton_OpenFile.clicked.connect(self.openbtn_click)
        self.pushButton__Remove.clicked.connect(self.deletebtn_click)
        self.pushButton_Extract.clicked.connect(self.extractbtn_click)
        self.pushButton_ExtractnOpen.clicked.connect(self.extractnopenbtn_click)
        self.pushButton_Log.clicked.connect(self.OpenLog)
        self.pushButton_Refresh.clicked.connect(self.refresh_list)
        #self.lineEdit_FileSearch.textChanged.connect(self.filter_changed)
        self.Running = False
        self.Stop = False

    #def filter_changed(self):
    #    self.filter = self.lineEdit_FileSearch.text()
    #    self.refresh_list()

    def OpenLog(self):
        f = open('log.txt', 'a')
        f.close()

        path = os.path.dirname(os.path.abspath(__file__)).replace('/', '\\')
        t = threading.Thread(target=FilePDFManager.OpenFile,
                             args=(path, 'log.txt'))
        t.start()

    def searchbtn_click(self):

        if self.Running == True:

            self.Stop = True
            self.Running = False
            self.label_progress.setText('STOP')
            return False

        if self.lineEdit_Search.text() == '':
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '빈 칸을 채워주세요')

        elif self.lineEdit_Path.text() == '':
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '폴더를 선택해주세요')

        elif self.lineEdit_page.text() == '':
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '빈 칸을 채워주세요')

        else:
            if self.Running == False:
                self.Running = True
                self.page = int(self.lineEdit_page.text())
                self.label_progress.setText('Downloading...')
                t = threading.Thread(target=self.download)
                t.daemon = True
                t.start()

    def download(self):

        path = self.lineEdit_Path.text().replace('/', '\\')
        keyword = self.lineEdit_Search.text()
        self.download_manager = Download_Manager(keyword=keyword, path=path, page_limit=self.page)

        while (1):
            self.refresh_list()
            flag = self.download_manager.download()

            if self.Stop == True:
                self.Stop = False
                break

            if flag == True:
                self.download_manager.page.DriverQuit()
                self.Running = False
                self.label_progress.setText('Done!')
                self.refresh_list()
                break

    def refresh_list(self):

        self.model.refresh()
        self.listView.setModel(self.model)
        self.listView.setRootIndex(self.model.index(self.path))

    def filebtn_click(self):

        fname = QtWidgets.QFileDialog.getExistingDirectory(MainWindow)
        self.lineEdit_Path.setText(fname)
        self.path = fname.replace('/', '\\')

        self.refresh_list()

    def deletebtn_click(self):

        try:
            filename = self.listView.currentIndex().data()
        except:
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '파일을 선택해주세요')
            return False

        if(filename == None):
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '파일을 선택해주세요')
            return False

        FilePDFManager.DeleteFile(self.path, filename)
        self.refresh_list()

    def extractbtn_click(self):

        if(self.lineEdit_Extract.text() == ''):
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '빈 칸을 채워주세요')
            return False

        elif(self.lineEdit_Extract_Line.text == ''):
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '빈 칸을 채워주세요')
            return False
        try:
            filename = self.listView.currentIndex().data()
        except:
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '파일을 선택해주세요')
            return False

        if (filename == None):
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '파일을 선택해주세요')
            return False

        line = int(self.lineEdit_Extract_Line.text())
        data = FilePDFManager.Extractor(self.path, filename,
                                        self.lineEdit_Extract.text(), line)
        filename = filename.split('.')[0]
        FilePDFManager.mktext(self.path, filename, data)

    def extractnopenbtn_click(self):

        if (self.lineEdit_Extract.text() == ''):
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '빈 칸을 채워주세요')
            return False

        elif (self.lineEdit_Extract_Line.text == ''):
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '빈 칸을 채워주세요')
            return False
        try:
            filename = self.listView.currentIndex().data()
        except:
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '파일을 선택해주세요')
            return False

        if (filename == None):
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '파일을 선택해주세요')
            return False

        line = int(self.lineEdit_Extract_Line.text())
        data = FilePDFManager.Extractor(self.path, filename,
                                        self.lineEdit_Extract.text(), line)
        filename = filename.split('.')[0]
        FilePDFManager.mktext(self.path, filename, data)

        t = threading.Thread(target=FilePDFManager.OpenFile,
                             args=(self.path, filename))
        t.start()

    def openbtn_click(self):

        filename = self.listView.currentIndex().data()
        print(self.listView.currentIndex().data())
        t = threading.Thread(target=FilePDFManager.OpenFile,
                             args=(self.path, filename))
        t.start()
        #FilePDFManager.OpenFile(self.path, filename)

    def __del__(self):
        self.download_manager.page.DriverQuit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#TODO 검색 히스토리 확인 기능 만들기, 추출하자마자 열기 버튼 만들기