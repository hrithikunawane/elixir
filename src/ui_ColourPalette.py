# ----------------------------------------------------------------------------------------------------------------------------------------------
# 23 June 2021 | 15 : 01 : 56 |
# ui_ColourPalette.py : User interface source for a colour palette.
# Prerequisite : PyQt5 [GPL version].
# Note : To perform a batch installation of the prerequisites of this project, run "pip3 install -r Requirements.txt" in the terminal.
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Imports
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PyQt5.QtGui import QCursor, QFont

# Constants
WINDOW_WIDTH = 854
WINDOW_HEIGHT = 580

# Defining a class for the colour palette ui
class Ui_ColourPalette(QtWidgets.QWidget):
    def setupUi(self, ColourPalette):
        ColourPalette.setObjectName(u"ColourPalette")
        ColourPalette.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Hex Code Labels
        self.HexCode01 = QtWidgets.QLabel(ColourPalette)
        self.HexCode01.setObjectName(u"HexCode01")
        self.HexCode01.setGeometry(QRect(10, 386, 208.5, 24))
        font01 = QFont()
        font01.setFamily(u"Poppins")
        font01.setPointSize(11)
        self.HexCode01.setFont(font01)
        self.HexCode01.setText(u"#FFFFFF")
        self.HexCode01.setStyleSheet(u"QLabel{\n"
"   color: rgb(134, 134, 134);\n"        
"}")
        self.HexCode01.setAlignment(Qt.AlignCenter)

        self.HexCode02 = QtWidgets.QLabel(ColourPalette)
        self.HexCode02.setObjectName(u"HexCode02")
        self.HexCode02.setGeometry(QRect(218.5, 386, 208.5, 24))
        self.HexCode02.setFont(font01)
        self.HexCode02.setText(u"#FFFFFF")
        self.HexCode02.setStyleSheet(u"QLabel{\n"
"   color: rgb(134, 134, 134);\n"        
"}")
        self.HexCode02.setAlignment(Qt.AlignCenter)

        self.HexCode03 = QtWidgets.QLabel(ColourPalette)
        self.HexCode03.setObjectName(u"HexCode03")
        self.HexCode03.setGeometry(QRect(427, 386, 208.5, 24))
        self.HexCode03.setFont(font01)
        self.HexCode03.setText(u"#FFFFFF")
        self.HexCode03.setStyleSheet(u"QLabel{\n"
"   color: rgb(134, 134, 134);"        
"}")
        self.HexCode03.setAlignment(Qt.AlignCenter)

        self.HexCode04 = QtWidgets.QLabel(ColourPalette)
        self.HexCode04.setObjectName(u"HexCode04")
        self.HexCode04.setGeometry(QRect(635.5, 386, 208.5, 24))
        self.HexCode04.setFont(font01)
        self.HexCode04.setText(u"#FFFFFF")
        self.HexCode04.setStyleSheet(u"QLabel{\n"
"   color: rgb(134, 134, 134);\n"        
"}")
        self.HexCode04.setAlignment(Qt.AlignCenter)

        # Buttons
        self.ExitBtn = QtWidgets.QPushButton(ColourPalette)
        self.ExitBtn.setObjectName(u"ExitBtn")
        self.ExitBtn.setGeometry(QRect(700, 500, 130, 50))
        font02 = QFont()
        font02.setFamily(u"Roboto")
        font02.setPointSize(10)
        self.ExitBtn.setFont(font02)
        self.ExitBtn.setText(u"Exit")
        self.ExitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ExitBtn.setStyleSheet(u"QPushButton{\n"
"   color: rgb(128, 128, 128);\n"        
"   background-color: rgb(214, 214, 214);\n"
"   border-style: None;\n"
"   border-radius: 02px;\n"
"}\n"
"\n"
"QPushButton::hover::!pressed{\n"
"   color: rgb(253, 253, 253);\n"
"   background-color: rgb(255, 64, 64);\n"
"}")

        self.ReloadBtn = QtWidgets.QPushButton(ColourPalette)
        self.ReloadBtn.setObjectName(u"ReloadBtn")
        self.ReloadBtn.setGeometry(QRect(562, 500, 130, 50))
        self.ReloadBtn.setFont(font02)
        self.ReloadBtn.setText(u"Reload")
        self.ReloadBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ReloadBtn.setStyleSheet(u"QPushButton{\n"
"   color: rgb(253, 253, 253);\n"        
"   background-color: rgb(112, 112, 112);\n"
"   border-style: None;\n"
"   border-radius: 02px;\n"
"}\n"
"\n"
"QPushButton::hover::!pressed{\n"
"   color: rgb(128, 128, 128);\n"
"   background-color: rgb(214, 214, 214);\n"
"}")

        self.retranslateUi(ColourPalette)

        QMetaObject.connectSlotsByName(ColourPalette)

    def retranslateUi(self, ColourPalette):
        ColourPalette.move(256, 94)
        ColourPalette.setWindowTitle(QCoreApplication.translate("ColourPalette", u"Colour Palette", None))
        ColourPalette.setWindowIcon(QtGui.QIcon(u"Elixir_Logo.png"))
        ColourPalette.setStyleSheet(u"background-color: rgb(246, 246, 246);")