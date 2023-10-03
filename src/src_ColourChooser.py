# ----------------------------------------------------------------------------------------------------------------------------------------------
# 23 June 2021 | 23 : 28 : 04 |
# src_ColourChooser.py : Responsible for rendering a custom colour palette.
# Prerequisite : Tkinter, PyQt5 [GPL version].
# Note : To perform a batch installation of the prerequisites of this project, run "pip3 install -r Requirements.txt" in the terminal.
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Imports
from tkinter import *
from tkinter import colorchooser
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow

# Colour Palette
from ui_ColourPalette import Ui_ColourPalette

# Constants
DEFAULT_SPACE = 4
PALETTE_WIDTH = 834
PALETTE_HEIGHT = 360

# Global
colours = []
hexcodes = []

# Defining a class for a custom colour palette
class ColourChooser(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ColourPalette()
        self.ui.setupUi(self)
        self.ChooseColour()

        # Pixmap setup
        self.modified = True
        self.mpixmap = QPixmap()
        self.function = (None, None)

        # INTERFACE SETUP

        # Removing title frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # Reading button events
        onclick_exit = self.ui.ExitBtn
        onclick_exit.clicked.connect(self.PostClick_Exit)

        onclick_reload = self.ui.ReloadBtn
        onclick_reload.clicked.connect(self.PostClick_Reload)

        # Displaying window
        self.show()

    # APP FUNCTIONS

    # Functions for quit/close action [If encountered]
    def PostClick_Exit(self):
        # Closing window
        self.close()

    # Function for reload action [If encountered]
    def PostClick_Reload(self):
        self.ChooseColour()
        self.function = (self.paintEvent, {})
        self.modified = True
        self.update()

    # Function for choosing custom colour
    def ChooseColour(self):
        root = Tk()
        root.geometry("+100+45")
        root.withdraw()

        global colours
        for i in range(DEFAULT_SPACE):
            colour_code = colorchooser.askcolor(title = "Colour Picker")
            colours.append(colour_code)
            # Converting the rgb value to the corresponding hex value
            hexval = "%02x%02x%02x" % colours[i]
            hexcodes.append("#" + str(hexval).upper())
    
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

    # Defining a function for generating a custom palette
    def DrawPalette(self, qpainter):
        # Setting hex code status
        self.ui.HexCode01.setText(hexcodes[0])
        self.ui.HexCode02.setText(hexcodes[1])
        self.ui.HexCode03.setText(hexcodes[2])
        self.ui.HexCode04.setText(hexcodes[3])

        for i in range(DEFAULT_SPACE):
            colour = QColor(*colours[i])
            qpainter.setPen(colour)
            qpainter.setBrush(QColor(colour))
            qpainter.drawRect(((int(PALETTE_WIDTH/DEFAULT_SPACE) * i) + 10), 10, 
            (int(PALETTE_WIDTH/DEFAULT_SPACE)), PALETTE_HEIGHT)

        # Clearing colours and hexcodes elements for a fresh run
        colours.clear()
        hexcodes.clear()