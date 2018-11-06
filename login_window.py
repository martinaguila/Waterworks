from PyQt4 import QtCore, QtGui
import mysql.connector
from menu_window import Ui_mainWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName(_fromUtf8("loginWindow"))
        loginWindow.resize(1440, 700)
        loginWindow.setWindowIcon(QtGui.QIcon('logo.jpg'))
        loginWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtGui.QWidget(loginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 120, 1431, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 220, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 290, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineUsername = QtGui.QLineEdit(self.centralwidget)
        self.lineUsername.setGeometry(QtCore.QRect(710, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(18)
        self.lineUsername.setFont(font)
        self.lineUsername.setText(_fromUtf8(""))
        self.lineUsername.setObjectName(_fromUtf8("lineUsername"))
        self.linePassword = QtGui.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(710, 290, 151, 31))
        self.linePassword.setEchoMode(QtGui.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(18)
        self.linePassword.setFont(font)
        self.linePassword.setObjectName(_fromUtf8("linePassword"))
        self.btnLogin = QtGui.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(760, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.btnLogin.clicked.connect(self.goToMainMenu)
        self.btnLogin.setStyleSheet("background-color: #1f70f2; color: white")
        self.btnExit = QtGui.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(640, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.btnExit.clicked.connect(self.exitApp)
        self.showPassword = QtGui.QCheckBox(self.centralwidget)
        self.showPassword.setGeometry(QtCore.QRect(870, 300, 111, 17))
        self.showPassword.stateChanged.connect(self.state_changed)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(10)
        self.showPassword.setFont(font)
        self.showPassword.setObjectName(_fromUtf8("showPassword"))
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        loginWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(loginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def goToMainMenu(self):
        user = self.lineUsername.text()
        password = self.linePassword.text()

        if user == "" or password == "":
            warningBox = QtGui.QMessageBox()
            warningBox.setText("Please insert your username and password before you login.")
            warningBox.setIcon(QtGui.QMessageBox.Warning)
            warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
            warningBox.setWindowTitle("San Pascual Waterworks")
            warningBox.exec_() 

            conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanjoseww")
            mycursor = conn.cursor()
            mycursor.execute('''SELECT * FROM user ''')
                
            data = mycursor.fetchall()

        else:
            conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanjoseww")
            mycursor = conn.cursor()
            mycursor.execute('''SELECT * FROM user ''')
            data = mycursor.fetchall()
            for data1 in data:
                if user == str(data1[1]) and password == str(data1[1]):
                    self.window = QtGui.QMainWindow()
                    self.ui = Ui_mainWindow()
                    self.ui.setupUi(self.window)
                    self.window.show()

                else:
                    warningBox = QtGui.QMessageBox()
                    warningBox.setText("Wrong username or password.")
                    warningBox.setIcon(QtGui.QMessageBox.Warning)
                    warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
                    warningBox.setWindowTitle("San Pascual Waterworks")
                    warningBox.exec_()
                        
        conn.commit()
        conn.close()  

    def state_changed(self):
        if self.showPassword.isChecked():
            self.linePassword.setEchoMode(QtGui.QLineEdit.Normal)       
        else:
            self.linePassword.setEchoMode(QtGui.QLineEdit.Password)

    def exitApp(self):
        self.window.close() 

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(_translate("loginWindow", "San Pascual Waterworks", None))
        self.label.setText(_translate("loginWindow", "SAN PASCUAL WATERWORKS", None))
        self.label_2.setText(_translate("loginWindow", "USERNAME", None))
        self.label_3.setText(_translate("loginWindow", "PASSWORD", None))
        self.btnLogin.setText(_translate("loginWindow", "LOGIN", None))
        self.btnExit.setText(_translate("loginWindow", "EXIT", None))
        self.showPassword.setText(_translate("loginWindow", "Show Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    loginWindow = QtGui.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

