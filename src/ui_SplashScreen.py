# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashScreenpKnHWH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(640, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadow = QFrame(self.centralwidget)
        self.DropShadow.setObjectName(u"DropShadow")
        self.DropShadow.setStyleSheet(u"QFrame{\n"
"	color: rgb(253, 253, 253);\n"
"	background-color: rgb(253, 253, 253);\n"
"	border-radius: 02px;\n"
"}")
        self.DropShadow.setFrameShape(QFrame.StyledPanel)
        self.DropShadow.setFrameShadow(QFrame.Raised)
        self.Title = QLabel(self.DropShadow)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(204, 40, 213, 77))
        font = QFont()
        font.setFamily(u"LEIXO")
        font.setPointSize(42)
        self.Title.setFont(font)
        self.Title.setStyleSheet(u"QLabel{\n"
"	color: rgb(112, 112, 112);\n"
"}")
        self.Title.setAlignment(Qt.AlignCenter)
        self.LoadingText = QLabel(self.DropShadow)
        self.LoadingText.setObjectName(u"LoadingText")
        self.LoadingText.setGeometry(QRect(0, 282, 620, 20))
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(10)
        self.LoadingText.setFont(font1)
        self.LoadingText.setStyleSheet(u"QLabel{\n"
"	color: rgb(112, 112, 112);\n"
"}")
        self.LoadingText.setAlignment(Qt.AlignCenter)
        self.ProgressBar = QProgressBar(self.DropShadow)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(60, 318, 500, 22))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        self.ProgressBar.setFont(font2)
        self.ProgressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(222, 222, 222);\n"
"	color: rgb(165, 165, 165);\n"
"	border-style: None;\n"
"	border-radius: 02px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: rgb(112, 112, 112);\n"
"	border-radius: 02px;\n"
"}")
        self.ProgressBar.setValue(24)
        self.ProgressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.DropShadow)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        SplashScreen.setWindowIcon(QIcon(u"Elixir_Logo.png"))
        self.Title.setText(QCoreApplication.translate("SplashScreen", u"ELIXIR", None))
        self.LoadingText.setText(QCoreApplication.translate("SplashScreen", u"Loading", None))
    # retranslateUi
