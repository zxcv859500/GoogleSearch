# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from Download_Manager import *
import FilePDFManager
import threading

class Ui_MainWindow(object):


    def __init__(self):

        self.Running = False

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(299, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.textEdit_Search = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Search = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_Search.setGeometry(QtCore.QRect(10, 10, 221, 21))
        #self.textEdit_Search.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.textEdit_Search.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_Search.setObjectName("textEdit_Search")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 51, 21))
        self.pushButton.setObjectName("pushButton")
        #self.textEdit_File = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_File = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_File.setGeometry(QtCore.QRect(70, 40, 161, 21))
        #self.textEdit_File.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.textEdit_File.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_File.setObjectName("textEdit_File")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(240, 40, 27, 18))
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 56, 20))
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 70, 280, 251))
        self.listView.setObjectName("listView")
        self.pushButton_Extract = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Extract.setGeometry(QtCore.QRect(240, 330, 51, 23))
        self.pushButton_Extract.setObjectName("pushButton_Extract")
        #self.textEdit_Search_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Search_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_Search_2.setGeometry(QtCore.QRect(10, 330, 221, 21))
        #self.textEdit_Search_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.textEdit_Search_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_Search_2.setObjectName("textEdit_Search_2")
        self.pushButton_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Delete.setGeometry(QtCore.QRect(240, 360, 50, 23))
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.searchbtn_click)
        self.pushButton_Delete.clicked.connect(self.deletebtn_click)
        self.pushButton_Extract.clicked.connect(self.extractbtn_click)
        self.toolButton.clicked.connect(self.filebtn_click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "저장경로"))
        self.pushButton_Extract.setText(_translate("MainWindow", "추출"))
        self.pushButton_Delete.setText(_translate("MainWindow", "삭제"))

    def searchbtn_click(self):

        if self.textEdit_Search.text() == '':
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '빈 칸을 채워주세요')

        elif self.textEdit_File.text() == '':
            QtWidgets.QMessageBox.about(MainWindow, 'Error', '폴더를 선택해주세요')

        else:
            if self.Running == False:
                self.Running = True
                t = threading.Thread(target=self.download)
                t.start()

    def download(self):

        path = self.textEdit_File.text().replace('/', '\\')
        keyword = self.textEdit_Search.text()
        download_manager = Download_Manager(keyword=keyword, path=path)

        while (1):
            ######self.refresh_list()
            flag = download_manager.download()

            if flag == True:
                download_manager.page.DriverQuit()
                self.Running = False
                break

    def filebtn_click(self):

        fname = QtWidgets.QFileDialog.getExistingDirectory(MainWindow)
        self.textEdit_File.setText(fname)
        self.path = fname

        self.refresh_list()

    def deletebtn_click(self):
        pass

    def extractbtn_click(self):
        pass

    def refresh_list(self):

        path = str(self.path)

        path.replace('/', '\\')

        file_list = FilePDFManager.GetFileList(path)

        for file in file_list:
            pass #여기까지

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

