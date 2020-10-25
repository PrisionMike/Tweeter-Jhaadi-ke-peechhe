# Our new main file. Being smart. Using the tweeting part as a procedure. not the GUI part.

from textotweet import tweetthetext
from guiclass import Newmainwin
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
twiwin = Newmainwin()
twiwin.show()
app.exec_()

