from PyQt4 import QtCore, QtGui
import mysql.connector
import pandas
import csv
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

class Ui_updateWindow(object):
    def setupUi(self, updateWindow):
        updateWindow.setObjectName(_fromUtf8("updateWindow"))
        updateWindow.resize(1440, 700)
        updateWindow.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.centralwidget = QtGui.QWidget(updateWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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
        self.lineMeter = QtGui.QLineEdit(self.centralwidget)
        self.lineMeter.setGeometry(QtCore.QRect(550, 150, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lineMeter.setFont(font)
        self.lineMeter.setText(_fromUtf8(""))
        self.lineMeter.setObjectName(_fromUtf8("lineMeter"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 411, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnSearch = QtGui.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(950, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.btnSearch.clicked.connect(self.searchDatabase)
        self.btnSearch.setStyleSheet("background-color: #1f70f2; color: white")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 270, 411, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 350, 411, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 430, 411, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineName = QtGui.QLineEdit(self.centralwidget)
        self.lineName.setGeometry(QtCore.QRect(710, 270, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lineName.setFont(font)
        self.lineName.setText(_fromUtf8(""))
        self.lineName.setObjectName(_fromUtf8("lineName"))
        self.linePhone = QtGui.QLineEdit(self.centralwidget)
        self.linePhone.setGeometry(QtCore.QRect(710, 350, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.linePhone.setFont(font)
        self.linePhone.setText(_fromUtf8(""))
        self.linePhone.setObjectName(_fromUtf8("linePhone"))
        self.lineAddress = QtGui.QLineEdit(self.centralwidget)
        self.lineAddress.setGeometry(QtCore.QRect(710, 430, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lineAddress.setFont(font)
        self.lineAddress.setText(_fromUtf8(""))
        self.lineAddress.setObjectName(_fromUtf8("lineAddress"))
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(940, 570, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName(_fromUtf8("btnBack"))
        self.btnBack.clicked.connect(self.updateDatabase)
        self.btnBack.setStyleSheet("background-color: #1f70f2; color: white")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 510, 411, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lbl_category = QtGui.QLabel(self.centralwidget)
        self.lbl_category.setGeometry(QtCore.QRect(710, 510, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lbl_category.setFont(font)
        self.lbl_category.setFrameShape(QtGui.QFrame.Box)
        self.lbl_category.setText(_fromUtf8(""))
        self.lbl_category.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_category.setObjectName(_fromUtf8("lbl_category"))
        updateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(updateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        updateWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(updateWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        updateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(updateWindow)
        QtCore.QMetaObject.connectSlotsByName(updateWindow)

    def searchDatabase(self):
        meter = self.lineMeter.text()

        if str(meter) == "":
            warningBox = QtGui.QMessageBox()
            warningBox.setText("Please enter Meter Number.")
            warningBox.setIcon(QtGui.QMessageBox.Warning)
            warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
            warningBox.setWindowTitle("San Pascual Waterworks")
            warningBox.exec_()

        else: 
            # conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="sanpascualww")
            conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
            mycursor = conn.cursor()

            mycursor.execute("SELECT * from clients WHERE meterNumber = " + '"' + (str(meter)) + '"')
            data = mycursor.fetchall()

        for name in data:
            self.lineName.setText(str(name[1]))
            self.linePhone.setText(str(name[2]))
            self.lineAddress.setText(str(name[3]))
            self.lbl_category.setText(str(name[4]))

            conn.commit()
            conn.close()

    def updateDatabase(self):
        meter = self.lineMeter.text()
        name = self.lineName.text()
        address = self.lineAddress.text()
        phone = self.linePhone.text()
        category = self.lbl_category.text()

        # conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="sanpascualww")
        conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
        mycursor2 = conn.cursor()

        mycursor2.execute("""INSERT INTO clients (meterNumber, Name, Address, Phone, Category) VALUES ("%s", "%s", "%s", "%s", "%s")"""
        % (str(meter), str(name), str(address), str(phone), str(category)))

        mycursor2.execute("""UPDATE clients set meterNumber=replace(meterNumber,'''','')""")
        mycursor2.execute("""UPDATE clients set Name=replace(Name,'''','')""")
        mycursor2.execute("""UPDATE clients set Address=replace(Address,'''','')""")
        mycursor2.execute("""UPDATE clients set Phone=replace(Phone,'''','')""")
        mycursor2.execute("""UPDATE clients set Category=replace(Category,'''','')""")

        # mycursor2.execute("""UPDATE customers SET Name = + "(str(name))" WHERE meterNumber = """ + '"' + (str(meter)) + '"')
        # mycursor2.execute("""UPDATE customers SET Name = () WHERE meterNumber = """ + '"' + (str(meter)) + '"' )

        table = pandas.read_sql('select * from clients', conn)
        table.to_csv('clients.csv', index=None)

        conn2 = sqlite3.connect('sanpascualww.db')
        c = conn2.cursor()

        c.execute('''DROP TABLE clients
                        ''')

        c.execute('''CREATE TABLE clients
                        (meterNumber integer, 
                        Name text,
                        Phone integer,
                        Address text,
                        Category text,
                        id integer PRIMARY KEY ON CONFLICT REPLACE)
                        ''')

        myclients = """INSERT INTO clients (meterNumber, Name, Phone, Address, Category, id) VALUES (?, ?, ?, ?, ?, ?)"""
        with open('clients.csv', 'r') as f:
                csv_data = csv.reader(f)
                csv_data.next()
                for row in csv_data:
                        c.execute(myclients, row)
                        conn2.commit()

        warningBox = QtGui.QMessageBox()
        warningBox.setText("An Account has been updated.")
        warningBox.setIcon(QtGui.QMessageBox.Information)
        warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
        warningBox.setWindowTitle("San Pascual Waterworks")
        warningBox.exec_()

        conn.commit()
        conn.close()

    def retranslateUi(self, updateWindow):
        updateWindow.setWindowTitle(_translate("updateWindow", "San Pascual Waterworks", None))
        self.label.setText(_translate("updateWindow", "San Pascual Waterworks", None))
        self.label_2.setText(_translate("updateWindow", "Update Accounts", None))
        self.label_3.setText(_translate("updateWindow", "Meter Number", None))
        self.btnSearch.setText(_translate("updateWindow", "SEARCH", None))
        self.label_4.setText(_translate("updateWindow", "Name", None))
        self.label_5.setText(_translate("updateWindow", "Phone Number", None))
        self.label_6.setText(_translate("updateWindow", "Address", None))
        self.btnBack.setText(_translate("updateWindow", "UPDATE", None))
        self.label_7.setText(_translate("updateWindow", "Category", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    updateWindow = QtGui.QMainWindow()
    ui = Ui_updateWindow()
    ui.setupUi(updateWindow)
    updateWindow.show()
    sys.exit(app.exec_())

