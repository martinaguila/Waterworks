from PyQt4 import QtCore, QtGui
from payment_window import Ui_paymentWindow
from accounts_window import Ui_accountWindow
import mysql.connector
import csv
import pandas
import sqlite3

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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1440, 700)
        mainWindow.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnAccounts = QtGui.QPushButton(self.centralwidget)
        self.btnAccounts.setGeometry(QtCore.QRect(430, 190, 581, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.btnAccounts.setFont(font)
        self.btnAccounts.setObjectName(_fromUtf8("btnAccounts"))
        self.btnAccounts.clicked.connect(self.accounts)
        self.btnAccounts.setStyleSheet("background-color: #1f70f2; color: white")
        self.btnTransaction = QtGui.QPushButton(self.centralwidget)
        self.btnTransaction.setGeometry(QtCore.QRect(430, 370, 581, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.btnTransaction.setFont(font)
        self.btnTransaction.setObjectName(_fromUtf8("btnTransaction"))
        self.btnTransaction.clicked.connect(self.transaction)
        self.btnTransaction.setStyleSheet("background-color: #1f70f2; color: white")
        self.btnExit = QtGui.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(910, 580, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        # self.btnExit.clicked.connect(self.exitApp)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1441, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 1441, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        conn2 = sqlite3.connect('sanpascualww.db')

        c = conn2.cursor()

        table1 = pandas.read_sql('select * from billing', sqlite3.connect('sanpascualww.db'))
        table1.to_csv('billing.csv', index=None)
        table1 = pandas.read_sql('select * from billing_first', sqlite3.connect('sanpascualww.db'))
        table1.to_csv('billing_first.csv', index=None)

        conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("""DROP TABLE billing""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS billing (BillingNumber INTEGER(20) AUTO_INCREMENT PRIMARY KEY, meterNumber INTEGER(20), Consumption INTEGER(20), BillingMonth VARCHAR(20), Year INTEGER(4), AmountDue INTEGER(20), Paid VARCHAR(10))""")
        mybilling = """INSERT INTO billing (BillingNumber, meterNumber, Consumption, BillingMonth, Year, AmountDue, Paid) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        with open('billing.csv', 'r') as f:
            csv_data = csv.reader(f)
            csv_data.next()
            for row in csv_data:
                cursor.execute(mybilling, row)
                conn.commit()

        cursor1.execute("""DROP TABLE billing_first""")
        cursor1.execute("""CREATE TABLE IF NOT EXISTS billing_first (meterNumber INTEGER(20), recent_billing INTEGER(20), new_billing INTEGER(20), Month VARCHAR(20), Year INTEGER(20), id INTEGER(20) AUTO_INCREMENT PRIMARY KEY)""")
        mybilling_first = """INSERT INTO billing_first (meterNumber, recent_billing, new_billing, Month, Year, id) VALUES (%s, %s, %s, %s, %s, %s)"""
        with open('billing_first.csv', 'r') as f:
            csv_data = csv.reader(f)
            csv_data.next()
            for row in csv_data:
                cursor1.execute(mybilling_first, row)
                conn.commit()

        cursor.close()
        cursor1.close()
        conn.close()

    def transaction(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_paymentWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def accounts(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_accountWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # def exitApp(self):
    #     self.destroy()

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "San Pascual Waterworks", None))
        self.btnAccounts.setText(_translate("mainWindow", "Manage Accounts", None))
        self.btnTransaction.setText(_translate("mainWindow", "Payment", None))
        self.btnExit.setText(_translate("mainWindow", "EXIT", None))
        self.label.setText(_translate("mainWindow", "San Pascual Waterworks", None))
        self.label_2.setText(_translate("mainWindow", "Main Menu", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

