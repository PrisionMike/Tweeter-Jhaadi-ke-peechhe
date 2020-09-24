from PyQt5 import QtCore,QtGui,QtWidgets
import sys

class Tweewin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.shouldtweet = False
        self.winsetup()

    def winsetup(self):

        self.setWindowTitle("Tweeter pop-up")
        self.resize(400,300)
        self.center()

        tweetbtn = QtWidgets.QPushButton('Tweet',self)
        tweetbtn.resize(tweetbtn.sizeHint())
        tweetbtn.move(100,100)
        tweetbtn.clicked.connect(self.showit)

        cancelbtn = QtWidgets.QPushButton('Cancel', self)
        cancelbtn.move(200,100)
        # cancelbtn.clicked.connect(QtWidgets.QApplication.instance().quit)
        cancelbtn.clicked.connect(self.close)
        cancelbtn.resize(cancelbtn.sizeHint())

        self.tweettext = ""
        self.txtbox = QtWidgets.QLineEdit(self)
        self.txtbox.move(50,50)
        self.txtbox.resize(280,40)

        # self.tweettxt,self.status = QtWidgets.QInputDialog.getText(self,'input dialog','haal kaisa hai janab ka?')
        self.show()
    
    def tweetit(self):
        self.tweettext = self.txtbox.text()
        if self.tweettext != ""
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

app = QtWidgets.QApplication(sys.argv)
twiwin = Tweewin()
# sys.exit(app.exec_())
app.exec_()
print('you maybe loooking for this:',twiwin.tweettext)

# print(twiwin.tweettxt,twiwin.status)