# So I just bought a book to learn GUI app development using PyQt5 and herein I'll attempt to build one step by step

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
from mkl_random import choice
import sys

windo_titties = [
    'Vo yaadein',
    'Vo lamhe',
    'Vo baatein',
    'Koi na jane',
    'Thi kaisi yadein',
    'O barsatein',
    'Whore nachan nu jee karda',
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ntimesclicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me")
        # button.setCheckable(True)
        self.button.clicked.connect(self.clickaction)
        # button.clicked.connect(self.willitworkbob)

        self.windowTitleChanged.connect(self.udghoshna)

        self.setCentralWidget(self.button)

        self.setFixedSize(QSize(400,300))

    def clickaction(self):
        print("Asshole!")
        newtitty = choice(windo_titties)
        print("New titty: ",newtitty)
        self.setWindowTitle(newtitty)

    def udghoshna(self,wintity):
        print("window titty: ",wintity)
        
        if wintity == windo_titties[-1]:
            self.button.setDisabled(True)
    # def willitworkbob(self,checked):
    #     print("Checked? ",checked,type(checked))
app = QApplication(sys.argv)
window = MainWindow()

# window = QWidget()
window.show()

app.exec_()