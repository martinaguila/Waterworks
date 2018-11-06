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

class Ui_addWindow(object):
    def setupUi(self, addWindow):
        addWindow.setObjectName(_fromUtf8("addWindow"))
        addWindow.resize(1440, 700)
        addWindow.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.centralwidget = QtGui.QWidget(addWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 1441, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1441, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 100, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 190, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 280, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineName = QtGui.QLineEdit(self.centralwidget)
        self.lineName.setGeometry(QtCore.QRect(720, 190, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lineName.setFont(font)
        self.lineName.setText(_fromUtf8(""))
        self.lineName.setObjectName(_fromUtf8("lineName"))
        self.linePhone = QtGui.QLineEdit(self.centralwidget)
        self.linePhone.setGeometry(QtCore.QRect(720, 280, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.linePhone.setFont(font)
        self.linePhone.setText(_fromUtf8(""))
        self.linePhone.setObjectName(_fromUtf8("linePhone"))
        # self.linePhone.setText("63")
        self.btnAdd = QtGui.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(720, 540, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.btnAdd.clicked.connect(self.addDatabase)
        self.btnAdd.setStyleSheet("background-color: #1f70f2; color: white")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(950, 540, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName(_fromUtf8("btnBack"))
        self.lineAddress = QtGui.QLineEdit(self.centralwidget)
        self.lineAddress.setGeometry(QtCore.QRect(720, 370, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lineAddress.setFont(font)
        self.lineAddress.setText(_fromUtf8(""))
        self.lineAddress.setObjectName(_fromUtf8("lineAddress"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 370, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 460, 471, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.radResidential = QtGui.QRadioButton(self.centralwidget)
        self.radResidential.setGeometry(QtCore.QRect(720, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(16)
        self.radResidential.setFont(font)
        self.radResidential.setObjectName(_fromUtf8("radResidential"))
        self.radCommercial = QtGui.QRadioButton(self.centralwidget)
        self.radCommercial.setGeometry(QtCore.QRect(920, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(16)
        self.radCommercial.setFont(font)
        self.radCommercial.setObjectName(_fromUtf8("radCommercial"))
        self.lblMeterNumber = QtGui.QLabel(self.centralwidget)
        self.lblMeterNumber.setGeometry(QtCore.QRect(720, 110, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblMeterNumber.setFont(font)
        self.lblMeterNumber.setFrameShape(QtGui.QFrame.Box)
        self.lblMeterNumber.setText(_fromUtf8(""))
        self.lblMeterNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMeterNumber.setObjectName(_fromUtf8("lblMeterNumber"))
        addWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(addWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        addWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(addWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        addWindow.setStatusBar(self.statusbar)

        self.retranslateUi(addWindow)
        QtCore.QMetaObject.connectSlotsByName(addWindow)

        # conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="sanpascualww")
        conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
        mycursor = conn.cursor()

        mycursor.execute("SELECT * from meter_counter")
        data = mycursor.fetchall()

        for count in data:
            add = int(str(count[0])) + 1

            self.lblMeterNumber.setText(str(add))

    def addDatabase(self):
        meter = self.lblMeterNumber.text()
        name = self.lineName.text()
        phone = self.linePhone.text()
        address = self.lineAddress.text()

        if str(meter) == "" or str(name) == "" or str(address) == "" or str(phone) == "":
            warningBox = QtGui.QMessageBox()
            warningBox.setText("Please fill all the fields.")
            warningBox.setIcon(QtGui.QMessageBox.Warning)
            warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
            warningBox.setWindowTitle("San Pascual Waterworks")
            warningBox.exec_()

        else:

            if self.radResidential.isChecked():

                # conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="sanpascualww")
                conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
                mycursor = conn.cursor()
                mycursor2 = conn.cursor()
                mycursor3 = conn.cursor()
                mycursor4 = conn.cursor()

                mycursor.execute("""INSERT INTO clients (meterNumber, Name, Address, Phone, Category) VALUES ("%s", "%s", "%s", "%s", "%s")"""
                    % (str(meter), str(name), str(address), int(phone), str("Residential")))

                mycursor2.execute("""INSERT INTO billing_first (meterNumber, recent_billing, new_billing, Month, Year) VALUES ("%s", "%s", "%s", "%s", "%s")"""
                    % (str(meter), int(0), int(0), str("none"), int(0)))

                mycursor3.execute("""INSERT INTO meter_counter (meterNumber) VALUES ("%s")"""
                    % (str(meter)))

                table = pandas.read_sql('select * from clients', conn)
                table.to_csv('clients.csv', index=None)
                table1 = pandas.read_sql('select * from billing_first', conn)
                table1.to_csv('billing_first.csv', index=None)

                conn2 = sqlite3.connect('sanpascualww.db')
                c = conn2.cursor()

            
                c.execute('''DROP TABLE billing_first
                        
                        ''')
                c.execute('''DROP TABLE clients
                        
                        ''')

                c.execute('''CREATE TABLE billing_first
                        (meterNumber text, 
                        recent_billing integer, 
                        new_billing integer,
                        Month text,
                        Year integer,
                        id integer PRIMARY KEY ON CONFLICT REPLACE)
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

                mybilling_first = """INSERT INTO billing_first (meterNumber, recent_billing, new_billing, Month, Year, id) VALUES (?, ?, ?, ?, ?, ?)"""
                with open('billing_first.csv', 'r') as f:
                        csv_data = csv.reader(f)
                        csv_data.next()
                        for row in csv_data:
                                c.execute(mybilling_first, row)
                                conn2.commit()

                warningBox = QtGui.QMessageBox()
                warningBox.setText("An account has been added.")
                warningBox.setIcon(QtGui.QMessageBox.Information)
                warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
                warningBox.setWindowTitle("San Pascual Waterworks")
                warningBox.exec_()

                self.lineName.clear()
                self.linePhone.clear()
                self.lineAddress.clear()

                mycursor4.execute("SELECT * from meter_counter")
                data = mycursor4.fetchall()

                for count in data:
                    add = int(str(count[0])) + 1

                    self.lblMeterNumber.setText(str(add))

                conn.commit()
                conn.close() 

            
            if self.radCommercial.isChecked():
            
                # conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="sanpascualww")
                conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
                mycursor = conn.cursor()
                mycursor2 = conn.cursor()
                mycursor3 = conn.cursor()
                mycursor4 = conn.cursor()

                mycursor.execute("""INSERT INTO clients (meterNumber, Name, Address, Phone, Category) VALUES ("%s", "%s", "%s", "%s", "%s")"""
                    % (str(meter), str(name), str(address), int(phone), str("Commercial")))

                mycursor2.execute("""INSERT INTO billing_first (meterNumber, recent_billing, new_billing, Month, Year) VALUES ("%s", "%s", "%s", "%s", "%s")"""
                    % (str(meter), int(0), int(0), str("none"), int(0)))

                mycursor3.execute("""INSERT INTO meter_counter (meterNumber) VALUES ("%s")"""
                    % (str(meter)))

                table = pandas.read_sql('select * from clients', conn)
                table.to_csv('clients.csv', index=None)
                table1 = pandas.read_sql('select * from billing_first', conn)
                table1.to_csv('billing_first.csv', index=None)

                conn2 = sqlite3.connect('sanpascualww.db')
                c = conn2.cursor()

            
                c.execute('''DROP TABLE billing_first
                        
                        ''')
                c.execute('''DROP TABLE clients
                        
                        ''')

                c.execute('''CREATE TABLE billing_first
                        (meterNumber text, 
                        recent_billing integer, 
                        new_billing integer,
                        Month text,
                        Year integer, 
                        id integer PRIMARY KEY ON CONFLICT REPLACE)
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

                mybilling_first = """INSERT INTO billing_first (meterNumber, recent_billing, new_billing, Month, Year, id) VALUES (?, ?, ?, ?, ?, ?)"""
                with open('billing_first.csv', 'r') as f:
                        csv_data = csv.reader(f)
                        csv_data.next()
                        for row in csv_data:
                                c.execute(mybilling_first, row)
                                conn2.commit()


                warningBox = QtGui.QMessageBox()
                warningBox.setText("An account has been added.")
                warningBox.setIcon(QtGui.QMessageBox.Information)
                warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
                warningBox.setWindowTitle("San Pascual Waterworks")
                warningBox.exec_()

                self.lineName.clear()
                self.linePhone.clear()
                self.lineAddress.clear()
                # self.linePhone.setText("63")

                mycursor4.execute("SELECT * from meter_counter")
                data = mycursor4.fetchall()

                for count in data:
                    add = int(str(count[0])) + 1

                    self.lblMeterNumber.setText(str(add))

                conn.commit()
                conn.close() 

    def retranslateUi(self, addWindow):
        addWindow.setWindowTitle(_translate("addWindow", "San Pascual Waterworks", None))
        self.label_2.setText(_translate("addWindow", "Add Accounts", None))
        self.label.setText(_translate("addWindow", "San Pascual Waterworks", None))
        self.label_3.setText(_translate("addWindow", "Meter Number", None))
        self.label_4.setText(_translate("addWindow", "Name", None))
        self.label_5.setText(_translate("addWindow", "Phone Number", None))
        self.btnAdd.setText(_translate("addWindow", "ADD", None))
        self.btnBack.setText(_translate("addWindow", "BACK", None))
        self.label_6.setText(_translate("addWindow", "Address", None))
        self.label_7.setText(_translate("addWindow", "Category", None))
        self.radResidential.setText(_translate("addWindow", "Residential", None))
        self.radCommercial.setText(_translate("addWindow", "Commercial", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    addWindow = QtGui.QMainWindow()
    ui = Ui_addWindow()
    ui.setupUi(addWindow)
    addWindow.show()
    sys.exit(app.exec_())

