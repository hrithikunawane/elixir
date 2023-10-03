# ----------------------------------------------------------------------------------------------------------------------------------------------
# 23 June 2021 | 15 : 50 : 30 |
# src_RandomPaletteGenerator.py : Responsible for generating a random colour scheme.
# Prerequisite : Pandas.
# Note : To perform a batch installation of the prerequisites of this project, run "pip3 install -r Requirements.txt" in the terminal.
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Imports
import sys
import random
import itertools
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

# Colour Palette
from ui_ColourPalette import Ui_ColourPalette

# Constants
DEFAULT_SPACE = 4
PALETTE_WIDTH = 834
PALETTE_HEIGHT = 360

CSV_PATH = "/home/buer/Additionals/Hrithik/Projects/Project 1/data/colours.csv"
INDEX = ["Colour", "Colour Name", "Hex Code", "Red", "Green", "Blue"]

# Defining a class for a palette render
class RandomColourPalette(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ColourPalette()
        self.ui.setupUi(self)

        # Pixmap setup
        self.modified = True
        self.mpixmap = QPixmap()
        self.function = (None, None)

        # Colour dataset setup
        self.temp = []
        self.colour_index = []
        self.df = pd.read_csv(CSV_PATH, names = INDEX, header = None)

        # INTERFACE SETUP

        # Removing title frame
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Reading button event
        onclick_exit = self.ui.ExitBtn
        onclick_exit.clicked.connect(self.PostClick_Exit)

        onclick_reload = self.ui.ReloadBtn
        onclick_reload.clicked.connect(self.PostClick_Reload)

        # Displaying window
        self.show()

    # APP FUNCTIONS

    # Function for quit/close action [If encountered]
    def PostClick_Exit(self):
        # Closing window
        self.close()

    # Function for reload action [If encountered]
    def PostClick_Reload(self):
        self.function = (self.paintEvent, {})
        self.modified = True
        self.update()

    # Paint event function
    def paintEvent(self, event):
        if self.modified:
            pixmap = QPixmap(self.size())
            pixmap.fill(QColor(246, 246, 246))
            qpainter = QPainter(pixmap)
            qpainter.drawPixmap(0, 0, self.mpixmap)
            self.DrawPalette(qpainter)
            self.mpixmap = pixmap
            self.modified = False

        qp = QPainter(self)
        qp.drawPixmap(0, 0, self.mpixmap)

    # Function for rendering a random colour scheme
    def DrawPalette(self, qpainter):
        temp = self.temp
        data_field = self.df
        colour_index = self.colour_index
        temp.append(random.sample(range(len(data_field)), k = DEFAULT_SPACE))
        colour_index = list(itertools.chain(*temp))

        # Setting hex code status
        self.ui.HexCode01.setText(str(data_field.loc[colour_index[0], "Hex Code"]).upper())
        self.ui.HexCode02.setText(str(data_field.loc[colour_index[1], "Hex Code"]).upper())
        self.ui.HexCode03.setText(str(data_field.loc[colour_index[2], "Hex Code"]).upper())
        self.ui.HexCode04.setText(str(data_field.loc[colour_index[3], "Hex Code"]).upper())

        # Generating random colours here
        for i in range(DEFAULT_SPACE):
            colr = QColor(data_field.loc[colour_index[i], "Red"],
            data_field.loc[colour_index[i], "Green"], data_field.loc[colour_index[i], "Blue"])
            qpainter.setPen(colr)
            qpainter.setBrush(colr)
            qpainter.drawRect(((int(PALETTE_WIDTH/DEFAULT_SPACE) * i) + 10), 10,
            (int(PALETTE_WIDTH/DEFAULT_SPACE)), PALETTE_HEIGHT)

        # Clearing temp after every call
        temp.clear()

# MAIN

if __name__ == "__main__":
    RandomPalette = QApplication(sys.argv)
    rndcp = RandomColourPalette()
    sys.exit(RandomPalette.exec_())