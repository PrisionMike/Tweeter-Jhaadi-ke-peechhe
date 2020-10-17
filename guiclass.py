from PyQt5 import QtCore,QtGui,QtWidgets
import sys
from textotweet import tweetthetext

class Mainwin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.shouldtweet = False
        self.siztup = (800,500)
        self.buttonleveloff = 100
        self.winsetup()

    def winsetup(self):

        self.setWindowTitle("Tweeter pop-up")
        self.resize(self.siztup[0],self.siztup[1])
        self.center()
        self.textfont = QtGui.QFont("Times",14)

        self.tweetbtn = QtWidgets.QPushButton('Tweet',self)
        self.tweetbtn.resize(self.tweetbtn.sizeHint())
        self.tweetbtn.move(self.buttonleveloff,self.siztup[1] - self.buttonleveloff)
        self.tweetbtn.setShortcut("Ctrl+Return")
        self.tweetbtn.clicked.connect(self.tweetit)

        cancelbtn = QtWidgets.QPushButton('Cancel', self)
        cancelbtn.move(4*self.buttonleveloff,self.siztup[1] - self.buttonleveloff)
        # cancelbtn.clicked.connect(QtWidgets.QApplication.instance().quit)
        cancelbtn.clicked.connect(self.close)
        cancelbtn.resize(cancelbtn.sizeHint())

        self.tweettext = ""

        self.txtbox = QtWidgets.QPlainTextEdit(self)
        self.txtbox.setFont(self.textfont)
        self.txtbox.setFocus()
        self.txtbox.move(10,10)
        self.txtbox.resize(self.siztup[0]-20,self.siztup[1]/2)

        # <<< === HERE'S THE SELF SHOW!!! === >>>
        # self.show()
    
    def tweetit(self):
        self.tweettext = self.txtbox.toPlainText()
        if self.tweettext != "":
            self.shouldtweet = True
            self.warnemptiness()
        else:
            tweetthetext(self.tweettext)
            self.txtbox.clear()


    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def warnemptiness(self):
        pass


# Comment this section before importing data
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    twiwin = Mainwin()
    app.exec_()
    print('you maybe loooking for this:',twiwin.tweettext)

# print(twiwin.tweettxt,twiwin.status)