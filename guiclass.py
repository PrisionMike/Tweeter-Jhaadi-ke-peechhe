from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton, QWidget, \
                            QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt5.QtCore import Qt
import sys
from textotweet import tweetthetext,ariri

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

        # self.setWindowTitle('Rab Raakha')
        self.resize(580,270)

        textfont = QtGui.QFont("Arial",14)
        btnfont = QtGui.QFont("OldEnglish",12)
        alertfont = QtGui.QFont("Times",12)
        headerfont = QtGui.QFont("Serif",10)

        self.shouldtweet = False        # No apparent use of this flag right now.
        self.tweettext = ""
        self.charlim = 240
        self.charwarn = 220

        mainlayout = QVBoxLayout()
        lowerlayout = QHBoxLayout()
        lowerleftlayout = QVBoxLayout()
        btnlayout = QGridLayout()

        self.charcount = QLabel("Char Limit:"+str(self.charlim))
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
        self.tweetbtn.clicked.connect(self.tweetit)
        self.tweetbtn.setFont(btnfont)
        self.tweetbtn.resize(2*self.tweetbtn.sizeHint())

        # mainlayout.addWidget(self.tweetbtn)

        self.cancelbtn = QtWidgets.QPushButton('Clear', self)
        self.cancelbtn.clicked.connect(self.cleanup)
        self.cancelbtn.setFont(btnfont)
        self.cancelbtn.resize(2*self.cancelbtn.sizeHint())

        # mainlayout.addWidget(self.cancelbtn)

        btnlayout.addWidget(self.tweetbtn,0,0)
        btnlayout.addWidget(self.cancelbtn,0,1)

        self.pkd = QtWidgets.QRadioButton("Paan Ki Dukaan", self)
        self.gkm = QtWidgets.QRadioButton("Gori Ka Makaan", self)
        self.pkd.toggled.connect(self.pkdfunk)
        self.gkm.toggled.connect(self.gkmfunc)
        self.pkd.setChecked(True)

        lowerleftlayout.addWidget(self.pkd)
        lowerleftlayout.addWidget(self.gkm)

        self.notiflabel = QLabel()
        self.notiflabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.notiflabel.setFont(alertfont)
        self.cleanup()

        lowerlayout.addWidget(self.notiflabel)

        self._setWindowtitle()

        widget = QWidget()
        widget.setLayout(mainlayout)
        self.setCentralWidget(widget)

    def _setWindowtitle(self):
        if self.appname.upper() == "PKD":
            self.setWindowTitle("Paan Ki Dukaan")
        if self.appname.upper() == "GKM":
            self.setWindowTitle("Gori Ka Makaan")

    def pkdfunk(self,s):
        if s:
            self.appname = "PKD"
        self._setWindowtitle()

    def gkmfunc(self,s):
        if s:
            self.appname = "GKM"
        self._setWindowtitle()

    def typing(self):
        txt = self.txtbox.toPlainText()
        tcount = len(txt)
        exclaim = ""
        if tcount < self.charwarn:
            self.charcount.setStyleSheet("color:Black")

        if tcount >= self.charwarn and tcount < self.charlim:
            self.charcount.setStyleSheet("color:Orange")
        if tcount >= self.charlim:
            self.charcount.setStyleSheet("color:Red;font:Bold")
            # self.charcount.setTextFormat()
            exclaim = "!"
            
        txtval = "Char Count:" + str(tcount) + "/" + str(self.charlim) + exclaim
        self.charcount.setText(txtval)

    def cleanup(self):
        self.shouldtweet = False
        # self.appname = "pkd"
        self.txtbox.clear()
        self.txtbox.setFocus()
        self.notiflabel.setText("Ready to Tweet")
        self.notiflabel.setStyleSheet("background-color:rgb(20,170,255)")
    
    def tweetit(self):
        self.tweettext = self.txtbox.toPlainText()
        if self.tweettext == "":
            self.shouldtweet = False
            self.warnemptiness()
        else:
            # tweetthetext(self.tweettext)
            # ariri(self.tweettext,self.appname)
            self.notiflabel.setText("Tweet Sent from\n"+self.appname)
            self.notiflabel.setStyleSheet("background-color:rgb(128,195,66)")
            self.txtbox.clear()
            self.txtbox.setFocus()
            # self.pkd.toggle()
            self.gkm.toggle()
    
    def warnemptiness(self):
        self.notiflabel.setStyleSheet("background-color:Yellow")
        self.notiflabel.setText("No Text. No Tweet.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    twiwin = Newmainwin()
    twiwin.show()
    app.exec_()