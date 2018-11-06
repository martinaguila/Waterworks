from PyQt4 import QtCore, QtGui
from datetime import datetime
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

class Ui_paymentWindow(object):
    def setupUi(self, paymentWindow):
        now = datetime.now()
        strg = now.strftime('%B %d, %Y')
        month = now.strftime('%B')
        day = now.strftime('%d')
        year = now.strftime('%Y')

        paymentWindow.setObjectName(_fromUtf8("paymentWindow"))
        paymentWindow.resize(1440, 700)
        paymentWindow.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.centralwidget = QtGui.QWidget(paymentWindow)
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
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 110, 711, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineMeter = QtGui.QLineEdit(self.centralwidget)
        self.lineMeter.setGeometry(QtCore.QRect(380, 170, 311, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lineMeter.setFont(font)
        self.lineMeter.setText(_fromUtf8(""))
        self.lineMeter.setObjectName(_fromUtf8("lineMeter"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 230, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineName = QtGui.QLabel(self.centralwidget)
        self.lineName.setGeometry(QtCore.QRect(380, 230, 311, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lineName.setFont(font)
        self.lineName.setText(_fromUtf8(""))
        self.lineName.setObjectName(_fromUtf8("lineName"))
        self.lineName.setFrameShape(QtGui.QFrame.Box)
        self.btnSearch = QtGui.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(380, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.btnSearch.clicked.connect(self.searchDatabase)
        self.btnSearch.setStyleSheet("background-color: #1f70f2; color: white")
        # self.btnSearchAll = QtGui.QPushButton(self.centralwidget)
        # self.btnSearchAll.setGeometry(QtCore.QRect(590, 290, 101, 41))
        # font = QtGui.QFont()
        # font.setFamily(_fromUtf8("MS Gothic"))
        # font.setPointSize(12)
        # self.btnSearchAll.setFont(font)
        # self.btnSearchAll.setObjectName(_fromUtf8("btnSearchAll"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 350, 591, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.itemClicked.connect(self.selectTable)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(700, 100, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 140, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(700, 180, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lblBill = QtGui.QLabel(self.centralwidget)
        self.lblBill.setGeometry(QtCore.QRect(1010, 100, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblBill.setFont(font)
        self.lblBill.setFrameShape(QtGui.QFrame.Box)
        self.lblBill.setText(_fromUtf8(""))
        self.lblBill.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBill.setObjectName(_fromUtf8("lblBill"))
        self.lblDate = QtGui.QLabel(self.centralwidget)
        self.lblDate.setGeometry(QtCore.QRect(1010, 180, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblDate.setFont(font)
        self.lblDate.setFrameShape(QtGui.QFrame.Box)
        self.lblDate.setText(_fromUtf8(""))
        self.lblDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDate.setObjectName(_fromUtf8("lblDate"))
        self.lblDate.setText(strg)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(700, 270, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 230, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(700, 310, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lblFor = QtGui.QLabel(self.centralwidget)
        self.lblFor.setGeometry(QtCore.QRect(1010, 230, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblFor.setFont(font)
        self.lblFor.setFrameShape(QtGui.QFrame.Box)
        self.lblFor.setText(_fromUtf8(""))
        self.lblFor.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFor.setObjectName(_fromUtf8("lblFor"))
        self.lblConsumption = QtGui.QLabel(self.centralwidget)
        self.lblConsumption.setGeometry(QtCore.QRect(1010, 270, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblConsumption.setFont(font)
        self.lblConsumption.setFrameShape(QtGui.QFrame.Box)
        self.lblConsumption.setText(_fromUtf8(""))
        self.lblConsumption.setAlignment(QtCore.Qt.AlignCenter)
        self.lblConsumption.setObjectName(_fromUtf8("lblConsumption"))
        self.lblStatus = QtGui.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(1010, 310, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblStatus.setFont(font)
        self.lblStatus.setFrameShape(QtGui.QFrame.Box)
        self.lblStatus.setText(_fromUtf8(""))
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        # self.btnCompute = QtGui.QPushButton(self.centralwidget)
        # self.btnCompute.setGeometry(QtCore.QRect(1010, 360, 101, 41))
        # font = QtGui.QFont()
        # font.setFamily(_fromUtf8("MS Gothic"))
        # font.setPointSize(12)
        # self.btnCompute.setFont(font)
        # self.btnCompute.setObjectName(_fromUtf8("btnCompute"))
        self.lblSub = QtGui.QLabel(self.centralwidget)
        self.lblSub.setGeometry(QtCore.QRect(1010, 450, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblSub.setFont(font)
        self.lblSub.setFrameShape(QtGui.QFrame.Box)
        self.lblSub.setText(_fromUtf8(""))
        self.lblSub.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSub.setObjectName(_fromUtf8("lblSub"))
        self.lblDue = QtGui.QLabel(self.centralwidget)
        self.lblDue.setGeometry(QtCore.QRect(1010, 410, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblDue.setFont(font)
        self.lblDue.setFrameShape(QtGui.QFrame.Box)
        self.lblDue.setText(_fromUtf8(""))
        self.lblDue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDue.setObjectName(_fromUtf8("lblDue"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(700, 410, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(700, 450, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_13.setFont(font)
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(700, 490, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.btnPrint = QtGui.QPushButton(self.centralwidget)
        self.btnPrint.setGeometry(QtCore.QRect(1010, 540, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnPrint.setFont(font)
        self.btnPrint.setObjectName(_fromUtf8("btnPrint"))
        self.btnPrint.clicked.connect(self.goPrint)
        self.btnPrint.setStyleSheet("background-color: #1f70f2; color: white")
        # self.lblPenalty = QtGui.QLabel(self.centralwidget)
        # self.lblPenalty.setGeometry(QtCore.QRect(740, 450, 211, 41))
        # font = QtGui.QFont()
        # font.setFamily(_fromUtf8("MS Gothic"))
        # font.setPointSize(22)
        # self.lblPenalty.setFont(font)
        # self.lblPenalty.setFrameShape(QtGui.QFrame.Box)
        # self.lblPenalty.setText(_fromUtf8(""))
        # self.lblPenalty.setAlignment(QtCore.Qt.AlignCenter)
        # self.lblPenalty.setObjectName(_fromUtf8("lblPenalty"))
        self.btnPrint_3 = QtGui.QPushButton(self.centralwidget)
        self.btnPrint_3.setGeometry(QtCore.QRect(1200, 540, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        self.btnPrint_3.setFont(font)
        self.btnPrint_3.setObjectName(_fromUtf8("btnPrint_3"))
        self.lblSub_2 = QtGui.QLabel(self.centralwidget)
        self.lblSub_2.setGeometry(QtCore.QRect(1010, 490, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblSub_2.setFont(font)
        self.lblSub_2.setFrameShape(QtGui.QFrame.Box)
        self.lblSub_2.setText(_fromUtf8(""))
        self.lblSub_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSub_2.setObjectName(_fromUtf8("lblSub_2"))
        self.lblORNum = QtGui.QLabel(self.centralwidget)
        self.lblORNum.setGeometry(QtCore.QRect(1010, 140, 291, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(22)
        self.lblORNum.setFont(font)
        self.lblORNum.setFrameShape(QtGui.QFrame.Box)
        self.lblORNum.setText(_fromUtf8(""))
        self.lblORNum.setAlignment(QtCore.Qt.AlignCenter)
        self.lblORNum.setObjectName(_fromUtf8("lblORNum"))
        paymentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(paymentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        paymentWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(paymentWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        paymentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(paymentWindow)
        QtCore.QMetaObject.connectSlotsByName(paymentWindow)

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
            mycursor2 = conn.cursor()

            mycursor2.execute("SELECT * from clients WHERE meterNumber = " + '"' + (str(meter)) + '"')
            data = mycursor.fetchall()

            for name in data:
                self.lineName.setText(str(name[1]))

            mycursor.execute('''SELECT * from billing WHERE Paid = "No" and meterNumber LIKE %s LIMIT 100''', ("" + str(meter) + "%",))
            
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(mycursor):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(data)))

            conn.commit()
            conn.close()

    def selectTable(self):

        now = datetime.now()
        strg = now.strftime('%B %d, %Y')
        month = now.strftime('%B')
        day = now.strftime('%d')
        year = now.strftime('%Y')


        bill = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()

        # conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="sanpascualww")
        conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
        mycursor = conn.cursor()
        mycursor1 = conn.cursor()
        mycursor2 = conn.cursor()

        mycursor2.execute("SELECT * from or_counter")
        data = mycursor2.fetchall()

        for count in data:
            add = int(str(count[1])) + 1

            self.lblORNum.setText(str(add))

        mycursor.execute('''SELECT * from billing WHERE BillingNumber LIKE %s LIMIT 100''', ("" + str(bill) + "%",))

        data = mycursor.fetchall()

        for name in data:
            self.lblBill.setText(str(name[0]))
            self.lblFor.setText(str(name[3]))
            self.lblConsumption.setText(str(name[2]))
            self.lblDue.setText(str(name[4]))

            if int(day) <= int(20):
                self.lblStatus.setText(str("Regular"))
                self.lblSub.setText(str("0"))

                self.lblSub_2.setText(str(name[4]))

            else:
                self.lblStatus.setText(str("Penalty"))
                

                # due = self.lblSub_2.setText(str(name[4]))
                due = self.lblDue.text()
                sub = int(str(due)) * .2

                self.lblSub.setText(str(sub))

                total = float(str(sub)) + int(str(due))

                self.lblSub_2.setText(str(total))

        conn.commit()
        conn.close()

    def goPrint(self):
        now = datetime.now()
        strg = now.strftime('%B %d, %Y')
        month = now.strftime('%B')

        bill = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()

        meter = self.lineMeter.text()
        or_num = self.lblORNum.text()
        cubic = self.lblConsumption.text()
        last_month = self.lblFor.text()
        amount = self.lblDue.text()
        penalty = self.lblSub.text()
        total_amount = self.lblSub_2.text()
        status = self.lblStatus.text()
        name = self.lineName.text()

        penalty = int(str(amount)) * .2

        # conn = mysql.connector.connect(host="localhost",user="root",passwd="",db="sanpascualww")
        conn = mysql.connector.connect(host="localhost",user="root",passwd="Martinluther01",db="sanpascualww")
        mycursor = conn.cursor()
        mycursor1 = conn.cursor()
        mycursor2 = conn.cursor()
        mycursor3 = conn.cursor()
        mycursor4 = conn.cursor()
        mycursor5 = conn.cursor()

        mycursor4.execute('''SELECT * from billing WHERE BillingNumber LIKE %s LIMIT 100''', ("" + str(bill) + "%",))

        data = mycursor4.fetchall()

        for name in data:
            mycursor1.execute('''UPDATE billing SET Paid = "Yes" WHERE BillingNumber = ''' + str(name[0]))

        mycursor3.execute('''SELECT * from billing_first WHERE meterNumber LIKE %s LIMIT 100''', ("" + str(meter) + "%",))

        data = mycursor3.fetchall()

        for name in data:
            previous = (str(name[1]))
            present = (str(name[2]))

        mycursor.execute("""INSERT INTO or_counter (OR_Num) VALUES ("%s")"""
            % (str(or_num)))

        if status == "Regular":         
            mycursor2.execute("""INSERT INTO client_records (Month, Pres_Reading, Prev_Reading, Cubic, Amount, Penalty, Total, OR_Num, Date_Iss, meterNumber) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""
                % (str(last_month), str(present), str(previous), str(cubic), str(amount), int(0), str(total_amount), str(or_num), str(strg), str(meter)))

        if status == "Penalty": 
            mycursor5.execute("""INSERT INTO client_records (Month, Pres_Reading, Prev_Reading, Cubic, Amount, Penalty, Total, OR_Num, Date_Iss, meterNumber) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""
                % (str(last_month), str(present), str(previous), str(cubic), str(amount), str(penalty), str(total_amount), str(or_num), str(strg), str(meter)))

        table = pandas.read_sql('select * from billing', conn)
        table.to_csv('billing.csv', index=None)

        conn2 = sqlite3.connect('sanpascualww.db')
        c = conn2.cursor()

    
        c.execute('''DROP TABLE billing
                
                ''')

        c.execute('''CREATE TABLE billing
            (BillingNumber integer PRIMARY KEY, 
            meterNumber text, 
            Consumption integer, 
            BillingMonth text, 
            Year integer, 
            AmountDue integer,
            Paid text)
            ''')

        mybilling = """INSERT INTO billing (BillingNumber, meterNumber, Consumption, BillingMonth, Year, AmountDue, Paid) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        with open('billing.csv', 'r') as f:
                csv_data = csv.reader(f)
                csv_data.next()
                for row in csv_data:
                        c.execute(mybilling, row)
                        conn2.commit()
        
        warningBox = QtGui.QMessageBox()
        warningBox.setText("Transaction is saved. Ready for printing.")
        warningBox.setIcon(QtGui.QMessageBox.Information)
        warningBox.setWindowIcon(QtGui.QIcon('/home/martin/THESIS/Qt Design/logo.jpg'))
        warningBox.setWindowTitle("San Pascual Waterworks")
        warningBox.exec_()

        self.lineMeter.clear()
        self.lblBill.clear()
        self.lblORNum.clear()
        self.lblFor.clear()
        self.lblConsumption.clear()
        self.lblStatus.clear()
        self.lblDue.clear()
        self.lblSub.clear()
        self.lblSub_2.clear()
        self.lineName.clear()

        conn.commit()
        conn.close()

        # words = num2words(float(total_amount))   
        
        # c = canvas.Canvas("receipt.pdf")
        # c.setLineWidth(.3)
        # c.setFont("Helvetica", 9)
        # c.setPageSize((308, 620))
        # c.drawString(135, 570, "San Pascual")
        # c.drawString(60, 515, str(strg))
        # c.drawString(60, 490, str(name))
        # c.drawString(60, 440, "Waterbill for")
        # c.drawString(80, 427, str(month) + "( " + str(con) + " c/m)")
        # c.drawString(207, 427, str(due) + "0") 
        # c.drawString(100, 414, str(what)) 
        # c.drawString(207, 414, str(much) + "0") 
        # c.drawString(207, 350, str(amt)+ "0")
        # c.drawString(60, 320, str(words) + " pesos only")
            
        # c.showPage()
        # c.save()

        # try:
        #     os.startfile("receipt.pdf")
        #     os.rename('temp1.pdf', 'receipt.pdf')
        # except:
        #     pass

    def retranslateUi(self, paymentWindow):
        paymentWindow.setWindowTitle(_translate("paymentWindow", "San Pascual Waterworks", None))
        self.label.setText(_translate("paymentWindow", "San Pascual Waterworks", None))
        self.label_2.setText(_translate("paymentWindow", "Payment", None))
        self.label_3.setText(_translate("paymentWindow", "Search Billing Records", None))
        self.label_4.setText(_translate("paymentWindow", "Meter Number", None))
        self.label_5.setText(_translate("paymentWindow", "Name", None))
        self.btnSearch.setText(_translate("paymentWindow", "SEARCH", None))
        # self.btnSearchAll.setText(_translate("paymentWindow", "SEARCH ALL", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("paymentWindow", "Billing Number", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("paymentWindow", "Meter Number ", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("paymentWindow", "Consumption", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("paymentWindow", "Billing Month", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("paymentWindow", "Amount Due", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("paymentWindow", "Paid", None))
        self.label_6.setText(_translate("paymentWindow", "Bill Number", None))
        self.label_7.setText(_translate("paymentWindow", "OR Number", None))
        self.label_8.setText(_translate("paymentWindow", "Date", None))
        self.label_9.setText(_translate("paymentWindow", "Consumption", None))
        self.label_10.setText(_translate("paymentWindow", "Waterbill For", None))
        self.label_11.setText(_translate("paymentWindow", "Status", None))
        # self.btnCompute.setText(_translate("paymentWindow", "COMPUTE", None))
        # self.label_12.setText(_translate("paymentWindow", "Amount Due", None))
        self.label_14.setText(_translate("paymentWindow", "Total", None))
        self.btnPrint.setText(_translate("paymentWindow", "PRINT", None))
        self.btnPrint_3.setText(_translate("paymentWindow", "BACK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    paymentWindow = QtGui.QMainWindow()
    ui = Ui_paymentWindow()
    ui.setupUi(paymentWindow)
    paymentWindow.show()
    sys.exit(app.exec_())

