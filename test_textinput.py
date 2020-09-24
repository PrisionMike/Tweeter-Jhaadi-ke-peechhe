from PyQt5 import QtCore,QtGui,QtWidgets
import sys

class Tweewin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
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
        cancelbtn.clicked.connect(QtWidgets.QApplication.instance().quit)
        cancelbtn.resize(cancelbtn.sizeHint())

        self.tweettext = ""
        self.txtbox = QtWidgets.QLineEdit(self)
        self.txtbox.move(50,50)
        self.txtbox.resize(280,40)

        # self.tweettxt,self.status = QtWidgets.QInputDialog.getText(self,'input dialog','haal kaisa hai janab ka?')
        self.show()
    
    def showit(self):
        self.tweettext = self.txtbox.text()
        print('the received tweet is',self.tweettxt)
        return self.tweettext

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

app = QtWidgets.QApplication(sys.argv)
twiwin = Tweewin()
print('you maybe loooking for this:',twiwin.tweettext)
sys.exit(app.exec_())
# print(twiwin.tweettxt,twiwin.status)