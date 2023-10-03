# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeScreenpatiDw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        if not HomeScreen.objectName():
            HomeScreen.setObjectName(u"HomeScreen")
        HomeScreen.resize(1180, 664)
        self.centralwidget = QWidget(HomeScreen)
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
        self.ElixirText = QLabel(self.DropShadow)
        self.ElixirText.setObjectName(u"ElixirText")
        self.ElixirText.setGeometry(QRect(20, 20, 70, 26))
        font = QFont()
        font.setFamily(u"LEIXO DEMO")
        font.setPointSize(14)
        self.ElixirText.setFont(font)
        self.ElixirText.setStyleSheet(u"QLabel{\n"
"	color: rgb(172, 172, 172);\n"
"}")
        self.ElixirText.setAlignment(Qt.AlignCenter)
        self.CloseBtn = QPushButton(self.DropShadow)
        self.CloseBtn.setObjectName(u"CloseBtn")
        self.CloseBtn.setGeometry(QRect(1088, 26, 48, 24))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(11)
        self.CloseBtn.setFont(font1)
        self.CloseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.CloseBtn.setMouseTracking(True)
        self.CloseBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(172, 172, 172);\n"
"	background-color: rgb(253, 253, 253);\n"
"	border-style: None;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(255, 64, 64);\n"
"}")
        self.CloseBtn.setFlat(False)
        self.WelcomeText = QLabel(self.DropShadow)
        self.WelcomeText.setObjectName(u"WelcomeText")
        self.WelcomeText.setGeometry(QRect(40, 80, 138, 40))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(24)
        self.WelcomeText.setFont(font2)
        self.WelcomeText.setStyleSheet(u"QLabel{\n"
"	color: rgb(112, 112, 112);\n"
"}")
        self.WelcomeText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.SubText = QLabel(self.DropShadow)
        self.SubText.setObjectName(u"SubText")
        self.SubText.setGeometry(QRect(40, 142, 872, 68))
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(10)
        self.SubText.setFont(font3)
        self.SubText.setStyleSheet(u"QLabel{\n"
"	color: rgb(172, 172, 172);\n"
"}")
        self.GetStartedText = QLabel(self.DropShadow)
        self.GetStartedText.setObjectName(u"GetStartedText")
        self.GetStartedText.setGeometry(QRect(40, 260, 130, 34))
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(18)
        self.GetStartedText.setFont(font4)
        self.GetStartedText.setStyleSheet(u"QLabel{\n"
"	color: rgb(112, 112, 112);\n"
"}")
        self.GetStartedText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.SubText_2 = QLabel(self.DropShadow)
        self.SubText_2.setObjectName(u"SubText_2")
        self.SubText_2.setGeometry(QRect(40, 300, 334, 24))
        self.SubText_2.setFont(font3)
        self.SubText_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(172, 172, 172);\n"
"}")
        self.RndmCP = QPushButton(self.DropShadow)
        self.RndmCP.setObjectName(u"RndmCP")
        self.RndmCP.setGeometry(QRect(136, 392, 125, 125))
        self.RndmCP.setCursor(QCursor(Qt.PointingHandCursor))
        self.RndmCP.setMouseTracking(True)
        self.RndmCP.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-style: None;\n"
"	border-radius: 08px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(112, 112, 112);\n"
"}\n"
"\n"
"QPushButton::hover::pressed{\n"
"	background-color: rgb(239, 239, 239);\n"
"}")
        icon = QIcon()
        icon.addFile(u"D:/Subject Dynamics Sem - 02/Machine Learning/Internal Project/Elixir/Assets/palette.png", 
        QSize(), QIcon.Normal, QIcon.Off)
        self.RndmCP.setIcon(icon)
        self.RndmCP.setIconSize(QSize(77, 77))
        self.ClrChsr = QPushButton(self.DropShadow)
        self.ClrChsr.setObjectName(u"ClrChsr")
        self.ClrChsr.setGeometry(QRect(538, 392, 125, 125))
        self.ClrChsr.setCursor(QCursor(Qt.PointingHandCursor))
        self.ClrChsr.setMouseTracking(True)
        self.ClrChsr.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-style: None;\n"
"	border-radius: 08px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(112, 112, 112);\n"
"}\n"
"\n"
"QPushButton::hover::pressed{\n"
"	background-color: rgb(239, 239, 239);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"D:/Subject Dynamics Sem - 02/Machine Learning/Internal Project/Elixir/Assets/color-picker.png", 
        QSize(), QIcon.Normal, QIcon.Off)
        self.ClrChsr.setIcon(icon1)
        self.ClrChsr.setIconSize(QSize(68, 68))
        self.ClrExtctr = QPushButton(self.DropShadow)
        self.ClrExtctr.setObjectName(u"ClrExtctr")
        self.ClrExtctr.setGeometry(QRect(940, 392, 125, 125))
        self.ClrExtctr.setCursor(QCursor(Qt.PointingHandCursor))
        self.ClrExtctr.setMouseTracking(True)
        self.ClrExtctr.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-style: None;\n"
"	border-radius: 08px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(112, 112, 112);\n"
"}\n"
"\n"
"QPushButton::hover::pressed{\n"
"	background-color: rgb(239, 239, 239);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"D:/Subject Dynamics Sem - 02/Machine Learning/Internal Project/Elixir/Assets/insert-picture-icon.png", 
        QSize(), QIcon.Normal, QIcon.Off)
        self.ClrExtctr.setIcon(icon2)
        self.ClrExtctr.setIconSize(QSize(75, 70))
        self.RndmCPText = QLabel(self.DropShadow)
        self.RndmCPText.setObjectName(u"RndmCPText")
        self.RndmCPText.setGeometry(QRect(116, 540, 164, 20))
        self.RndmCPText.setFont(font1)
        self.RndmCPText.setStyleSheet(u"QLabel{\n"
"	color: rgb(112, 112, 112);\n"
"}")
        self.RndmCPText.setAlignment(Qt.AlignCenter)
        self.ClrChsrText = QLabel(self.DropShadow)
        self.ClrChsrText.setObjectName(u"ClrChsrText")
        self.ClrChsrText.setGeometry(QRect(546, 540, 110, 20))
        self.ClrChsrText.setFont(font1)
        self.ClrChsrText.setStyleSheet(u"QLabel{\n"
"	color: rgb(112, 112, 112);\n"
"}")
        self.ClrChsrText.setAlignment(Qt.AlignCenter)
        self.ClrExtctrText = QLabel(self.DropShadow)
        self.ClrExtctrText.setObjectName(u"ClrExtctrText")
        self.ClrExtctrText.setGeometry(QRect(945, 540, 115, 20))
        self.ClrExtctrText.setFont(font1)
        self.ClrExtctrText.setStyleSheet(u"QLabel{\n"
"	color: rgb(112, 112, 112);\n"
"}")
        self.ClrExtctrText.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.DropShadow)

        HomeScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeScreen)

        QMetaObject.connectSlotsByName(HomeScreen)
    # setupUi

    def retranslateUi(self, HomeScreen):
        HomeScreen.setWindowTitle(QCoreApplication.translate("HomeScreen", u"MainWindow", None))
        HomeScreen.setWindowIcon(QIcon(u"Elixir_Logo.png"))
        self.ElixirText.setText(QCoreApplication.translate("HomeScreen", u"ELIXIR", None))
        self.CloseBtn.setText(QCoreApplication.translate("HomeScreen", u"CLOSE", None))
        self.WelcomeText.setText(QCoreApplication.translate("HomeScreen", u"Welcome", None))
        self.SubText.setText(QCoreApplication.translate("HomeScreen", u"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard \n"
"dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen \n"
"book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.", None))
        self.GetStartedText.setText(QCoreApplication.translate("HomeScreen", u"Get Started", None))
        self.SubText_2.setText(QCoreApplication.translate("HomeScreen", u"Render an awesome colour palette for your project.", None))
        self.RndmCP.setText("")
        self.ClrChsr.setText("")
        self.ClrExtctr.setText("")
        self.RndmCPText.setText(QCoreApplication.translate("HomeScreen", u"Random Colour Palette", None))
        self.ClrChsrText.setText(QCoreApplication.translate("HomeScreen", u"Colour Chooser", None))
        self.ClrExtctrText.setText(QCoreApplication.translate("HomeScreen", u"Colour Extractor", None))
    # retranslateUi
