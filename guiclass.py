from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import Qt
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
        self.btnfont = QtGui.QFont("Arial",12)
        self.alertfont = QtGui.QFont("Times",12)

        self.tweetbtn = QtWidgets.QPushButton('Tweet',self)
        self.tweetbtn.move(self.buttonleveloff,self.siztup[1] - self.buttonleveloff)
        self.tweetbtn.setShortcut("Ctrl+Return")
        self.tweetbtn.clicked.connect(self.tweetit)
        self.tweetbtn.setFont(self.btnfont)
        self.tweetbtn.resize(2*self.tweetbtn.sizeHint())

        self.cancelbtn = QtWidgets.QPushButton('Cancel', self)
        self.cancelbtn.move(4*self.buttonleveloff,self.siztup[1] - self.buttonleveloff)
        self.cancelbtn.clicked.connect(self.close)
        self.cancelbtn.setFont(self.btnfont)
        self.cancelbtn.resize(2*self.cancelbtn.sizeHint())

        self.tweettext = ""

        self.txtbox = QtWidgets.QPlainTextEdit(self)
        self.txtbox.setFont(self.textfont)
        self.txtbox.setFocus()
        self.txtbox.move(10,10)
        self.txtbox.resize(self.siztup[0]-20,int(self.siztup[1]/2))

        self.alertbox = QtWidgets.QLabel("XXXXXXXXXXXXXXXXXXXXXX")
        fontalert = self.alertbox.font()
        fontalert.setPointSize(30)
        self.alertbox.setFont(fontalert)
        # self.alertbox.setFont(self.alertfont)
        # self.alertbox.setText("Any wellcome here?")
        # self.alertbox.setStyleSheet("color:yellow")
        self.alertbox.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.alertbox.move(400,250)
        # self.alertbox.setGeometry(10,400,300,100)
        # self.alertbox.show()


        # <<< === HERE'S THE SELF SHOW!!! === >>>
        # self.show()
    
    def tweetit(self):
        self.tweettext = self.txtbox.toPlainText()
        if self.tweettext == "":
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



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    twiwin = Mainwin()
    twiwin.show()
    app.exec_()
    print('you maybe loooking for this:',twiwin.tweettext)

# print(twiwin.tweettxt,twiwin.status)