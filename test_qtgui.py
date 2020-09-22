import sys
from PyQt5.QtWidgets import QApplication as qap, QWidget as qw, QPushButton as qpb, \
    QDesktopWidget as qdw 
from PyQt5.QtGui import QIcon as qico 

# print("sys.argv returns:\n",sys.argv)

class typwidge(qw):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        twbtn = qpb('Tweet',self)
        twbtn.resize(twbtn.sizeHint())
        twbtn.move(100,100)
        
        qbtn = qpb('quit',self)
        qbtn.move(50,100)
        qbtn.clicked.connect(qap.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200,100)

        # self.setGeometry(300,300,350,250)
        self.setWindowTitle('Humaari Krishna')
        # self.setWindowIcon(qico('.\\appico.png'))
        self.resize(400,300)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = qdw().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = qap(sys.argv)
w = typwidge()
# w.resize(450,150)
# w.move(300,300)
# w.setWindowTitle('Tweeterbhai Jhadiwala')
# w.show()

sys.exit(app.exec_())