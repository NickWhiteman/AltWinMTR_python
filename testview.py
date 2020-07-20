#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #Кнопка выход---------
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(800, 20)
        #------------------
        #Кнопка пинг
        qbping = QPushButton('Ping', self)
        qbping.setCheckable(True)
        qbping.move(50, 50)
        #Кнопка трасерт
        qbtracert = QPushButton('Tracert', self)
        qbtracert.setCheckable(True)
        qbtracert.move(160, 50)
        #Поле для ip
        self.le = QLineEdit(self)
        self.le.move(30, 22)


        self.resize(900, 420)#размер_выравнивание
        self.center() #Центрирование
        self.setWindowTitle('Alt_WINMTR') #Название окна
        self.setWindowIcon(QIcon('images/icons.png')) #Иконка
        self.setWindowTitle('Quit button') #Кнопка выход
        self.show()

    def closeEvent(self, event): #окно подтверждения закрытия и закрытие.
        reply = QMessageBox.question(self, 'Exit',"Вы точно хотите выйти?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())