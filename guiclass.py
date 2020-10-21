from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton, QWidget, \
                            QVBoxLayout,QHBoxLayout,QGridLayout
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

        self.alertbox = QtWidgets.QLabel("XXXXXXXXXXXXXXXXXXXXXX",self)
        fontalert = self.alertbox.font()
        fontalert.setPointSize(14)
        self.alertbox.setFont(fontalert)
        # self.alertbox.setFont(self.alertfont)
        self.alertbox.setText("Any wellcome here?")
        self.alertbox.setStyleSheet("color:Orange")
        # self.alertbox.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.alertbox.move(300,300)
        # self.alertbox.setGeometry(10,400,300,100)
    
    def tweetit(self):
        self.tweettext = self.txtbox.toPlainText()
        if self.tweettext == "":
            self.shouldtweet = True
            self.warnemptiness()
        else:
            tweetthetext(self.tweettext)
            self.alertbox.setText("Tweet Sent!")
            self.alertbox.setStyleSheet("color:Blue")
            self.txtbox.clear()


    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def warnemptiness(self):
        pass


# New Class preferred class.
class Newmainwin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Rab Raakha')
        self.resize(750,420)

        textfont = QtGui.QFont("Arial",14)
        btnfont = QtGui.QFont("OldEnglish",12)
        alertfont = QtGui.QFont("Times",12)
        headerfont = QtGui.QFont("Serif",10)
        
        mainlayout = QVBoxLayout()
        lowerlayout = QHBoxLayout()
        lowerleftlayout = QVBoxLayout()
        btnlayout = QGridLayout()

        self.charcount = QLabel("Char Limit:240")
        self.charcount.setFont(headerfont)
        self.charcount.setAlignment(Qt.AlignRight)

        mainlayout.addWidget(self.charcount)

        self.txtbox = QtWidgets.QPlainTextEdit(self)
        self.txtbox.setFont(textfont)
        self.txtbox.setFocus()
        self.txtbox.setAutoFillBackground(True)
        self.txtbox.textChanged.connect(self.typing)

        mainlayout.addWidget(self.txtbox)

        mainlayout.addLayout(lowerlayout)
        lowerlayout.addLayout(lowerleftlayout)
        lowerleftlayout.addLayout(btnlayout)

        self.tweetbtn = QtWidgets.QPushButton('Tweet',self)
        self.tweetbtn.setShortcut("Ctrl+Return")
        # self.tweetbtn.clicked.connect(self.tweetit)
        self.tweetbtn.setFont(btnfont)
        self.tweetbtn.resize(2*self.tweetbtn.sizeHint())

        # mainlayout.addWidget(self.tweetbtn)

        self.cancelbtn = QtWidgets.QPushButton('Clear', self)
        self.cancelbtn.clicked.connect(self.txtbox.clear)
        self.cancelbtn.setFont(btnfont)
        self.cancelbtn.resize(2*self.cancelbtn.sizeHint())

        # mainlayout.addWidget(self.cancelbtn)

        btnlayout.addWidget(self.tweetbtn,0,0)
        btnlayout.addWidget(self.cancelbtn,0,2)

        widget = QWidget()
        widget.setLayout(mainlayout)
        self.setCentralWidget(widget)

    def typing(self):
        charlim = 100
        charwarn = 80
        txt = self.txtbox.toPlainText()
        tcount = len(txt)
        exclaim = ""
        if tcount < charwarn:
            self.charcount.setStyleSheet("color:Black")

        if tcount >= charwarn and tcount < charlim:
            self.charcount.setStyleSheet("color:Orange")
        if tcount >= charlim:
            self.charcount.setStyleSheet("color:Red;font:Bold")
            # self.charcount.setTextFormat()
            exclaim = "!"
            
        txtval = "Char Count:" + str(tcount) + "/" + str(charlim) + exclaim
        self.charcount.setText(txtval)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    twiwin = Newmainwin()
    twiwin.show()
    app.exec_()
    # print('you maybe loooking for this:',twiwin.tweettext)

# print(twiwin.tweettxt,twiwin.status)