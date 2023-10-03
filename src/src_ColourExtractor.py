# ----------------------------------------------------------------------------------------------------------------------------------------------
# 24 June 2021 | 00 : 00 : 00 |
# src_ColourExtractor.py : Responsible for extracting colours from a reference.
# Prerequisite : Colorgram, PyQt5 [GPL version].
# Note : To perform a batch installation of the prerequisites of this project, run "pip3 install -r Requirements.txt" in the terminal.
# ----------------------------------------------------------------------------------------------------------------------------------------------

# Imports
import colorgram
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog

# Colour Palette
from ui_ColourPalette import Ui_ColourPalette

# Constants
DEFAULT_SPACE = 4
PALETTE_WIDTH = 834
PALETTE_HEIGHT = 360

# Globals
colours = []
colour_att = ()
fileinfo = ""
hexcodes = []

# Defining a class for colour extraction
class ColourExtract(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ColourPalette()
        self.ui.setupUi(self)
        self.ExtractColours()

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

    # Function for quit/close action [If encountered]
    def PostClick_Exit(self):
        # Closing window
        self.close()

    # Function for reload action [If encountered]
    def PostClick_Reload(self):
        self.ExtractColours()
        self.function = (self.paintEvent, {})
        self.modified = True
        self.update()

    # Function for extracting colours
    def ExtractColours(self):
        global colours
        fileinfo = QFileDialog.getOpenFileName(self, "Select Reference")
        filename = str(fileinfo[0])
        colours = colorgram.extract(filename, DEFAULT_SPACE)

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

    # Defining a function for generating the colour palette
    def DrawPalette(self, qpainter):
        for i in range(DEFAULT_SPACE):
            colour_att = colours[i]
            red = colour_att.rgb.r
            green = colour_att.rgb.g
            blue = colour_att.rgb.b
            
            # Converting rgb to hex
            hexvalue = "%02x%02x%02x" % (red, green, blue)
            hexcodes.append("#" + str(hexvalue).upper())

            # Rendering the colour palette here
            colour = QColor(red, green, blue)
            qpainter.setPen(colour)
            qpainter.setBrush(QColor(colour))
            qpainter.drawRect(((int(PALETTE_WIDTH/DEFAULT_SPACE) * i) + 10), 10,
            (int(PALETTE_WIDTH/DEFAULT_SPACE)), PALETTE_HEIGHT)

        # Setting hex code status
        self.ui.HexCode01.setText(hexcodes[0])
        self.ui.HexCode02.setText(hexcodes[1])
        self.ui.HexCode03.setText(hexcodes[2])
        self.ui.HexCode04.setText(hexcodes[3])

        # Clearing colours and hexcodes elements for a fresh run
        colours.clear()
        hexcodes.clear()