from PyQt5 import QtCore,QtGui,QtWidgets
import sys

class Tweewin(QtWidgets.QWidget):
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

        tweetbtn = QtWidgets.QPushButton('Tweet',self)
        tweetbtn.resize(tweetbtn.sizeHint())
        tweetbtn.move(self.buttonleveloff,self.siztup[1] - self.buttonleveloff)
        tweetbtn.setShortcut("Ctrl+Return")
        tweetbtn.clicked.connect(self.tweetit)

        cancelbtn = QtWidgets.QPushButton('Cancel', self)
        cancelbtn.move(4*self.buttonleveloff,self.siztup[1] - self.buttonleveloff)
        # cancelbtn.clicked.connect(QtWidgets.QApplication.instance().quit)
        cancelbtn.clicked.connect(self.close)
        cancelbtn.resize(cancelbtn.sizeHint())

        self.tweettext = ""
        # self.txtbox = QtWidgets.QLineEdit(self)
        self.txtbox = QtWidgets.QPlainTextEdit(self)
        # self.txtbox.returnPressed.connect(self.tweetit)
        self.txtbox.setFont(self.textfont)
        self.txtbox.setFocus()
        self.txtbox.move(10,10)
        self.txtbox.resize(self.siztup[0]-20,self.siztup[1]/2)

        # self.tweettxt,self.status = QtWidgets.QInputDialog.getText(self,'input dialog','haal kaisa hai janab ka?')
        self.show()
    
    def tweetit(self):
        self.tweettext = self.txtbox.toPlainText()
        if self.tweettext != "":
            self.shouldtweet = True
        # print('the received tweet is',self.tweettext)
        # QtWidgets.QApplication.instance().quit
        self.close()
        # return self.tweettext

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# Comment this section before importing data
# app = QtWidgets.QApplication(sys.argv)
# twiwin = Tweewin()
# # sys.exit(app.exec_())
# app.exec_()
# print('you maybe loooking for this:',twiwin.tweettext)

# print(twiwin.tweettxt,twiwin.status)