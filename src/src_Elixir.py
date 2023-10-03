# ----------------------------------------------------------------------------------------------------------------------------------------------
# 23 June 2021 | 12 : 17 : 30 |
# src_Elixir.py : Initializer of splash screen and home screen.
# Prerequisite : PySide2.
# UI Sources : ui_SplashScreen.py, ui_HomeScreen.py.
# Note : To perform a batch installation of the prerequisites of this project, run "pip3 install -r Requirements.txt" in the terminal.
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Imports
import sys
import time
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import QColor

# Splash Screen
from ui_SplashScreen import Ui_SplashScreen

# Home Screen
from ui_HomeScreen import Ui_HomeScreen

# Random Palette Generator
from RandomPaletteGenerator import RandomColourPalette

# Colour Chooser
from ColourChooser import ColourChooser

# Colour Extractor
from ColourExtractor import ColourExtract

# Global
count_prog = 0

# Defining a class for splash screen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # INTERFACE SETUP

        # Drop shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.DropShadow.setGraphicsEffect(self.shadow)

        # Removing title frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Qtimer start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.SetProgress)
        self.timer.start(35)

        # Changing loading status
        QtCore.QTimer.singleShot(2280, lambda : self.ui.LoadingText.setText("Importing Requisites"))
        QtCore.QTimer.singleShot(2800, lambda : self.ui.LoadingText.setText("Setting Up Environment"))
        QtCore.QTimer.singleShot(3600, lambda : self.ui.LoadingText.setText("Saving Shadow Log"))
        QtCore.QTimer.singleShot(5000, lambda : self.ui.LoadingText.setText("Getting Interface Ready"))
        QtCore.QTimer.singleShot(6000, lambda : self.ui.LoadingText.setText("Launching Home Screen"))

        # Display splash screen
        self.show()

    # APP FUNCTIONS

    # Function for updating the progress bar
    def SetProgress(self):
        global count_prog

        # Setting values to progress bar
        self.ui.ProgressBar.setValue(count_prog)

        # Dramatic counting
        if count_prog >= 32 and count_prog <= 34:
            time.sleep(0.42)

        # Closing splash screen after completion
        if count_prog > 100:
            self.timer.stop()

            # Displaying home screen here
            self.home = HomeScreen()
            time.sleep(0.08)
            self.home.show()

            # Closing splash screen
            self.close()

        # Incrementing counter variable with unit value
        count_prog +=1

# Defining a class for home screen
class HomeScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_HomeScreen()
        self.ui.setupUi(self)

        # INTERFACE SETUP

        # Drop shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.DropShadow.setGraphicsEffect(self.shadow)

        # Removing title frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Getting close button status [If encountered]
        onclick_close = self.ui.CloseBtn
        onclick_close.clicked.connect(self.PostClick_Close)

        # Getting RPG button status [If encountered]
        onclick_rpg = self.ui.RndmCP
        onclick_rpg.clicked.connect(self.PostClick_RPG)

        # Getting CC button status [If encountered]
        onclick_cc = self.ui.ClrChsr
        onclick_cc.clicked.connect(self.PostClick_CC)

        # Getting CE button status [If encountered]
        onclick_ce = self.ui.ClrExtctr
        onclick_ce.clicked.connect(self.PostClick_CE)

    # APP FUNCTIONS

    # Function defining quit/close action
    def PostClick_Close(self):
        # Quitting with exit code 0
        exit(0)

    # Function defining rpg action
    def PostClick_RPG(self):
        # Generating a random palette here
        self.rpg = RandomColourPalette()

    # Function defining cc action
    def PostClick_CC(self):
        # Generating a custom palette here
        self.cc = ColourChooser()

    # Function defining ce action
    def PostClick_CE(self):
        # Generating a inspired colour palette here
        self.ce = ColourExtract()

# MAIN

if __name__ == "__main__":
    Elixir = QApplication(sys.argv)
    Window = SplashScreen()
    sys.exit(Elixir.exec_())