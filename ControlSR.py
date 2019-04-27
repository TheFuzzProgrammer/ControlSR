# Created by fuzz at 25/4/19
"""This compilation / file uses a Open Source licence, most of developers,
in a part of their lives, uses some software that have it too, so, as you
know, you are part of that developers, from the Open Source community
we have loved of that, and it will great to someday we can use some contribution from you
from you, thanks for be part of this"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
import argparse
import pickle

print(sys.argv)


class Main_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        try:
            if len(sys.argv) == 2:
                if sys.argv[1]=="s":
                    uic.loadUi("ui/setup.ui", self)
            else:
                uic.loadUi("ui/starter.ui", self)
        except:
            uic.loadUi("ui/starter.ui", self)
        self.setWindowTitle('ControlSR')
        self.userinput.setText('User')
        self.passinput.setText('Password')
        self.userlabel.setText('')
        self.session_starter.setText('Start Session')


app = QApplication(sys.argv)
_ventana = Main_Window()
_ventana.show()
app.exec_()
