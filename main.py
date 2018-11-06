import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
import sqlite3
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from datetime import datetime
# from twilio.rest import Client

Builder.load_string("""

<HomeScreen>:
	BoxLayout:
		orientation: 'vertical'
		Label:
			text: 'San Pascual WaterWorks'		
			font_size: 45
		Label:
			text: ''
			font_size: 45
		Label:
			text: 'Username'
			font_size: 45
		TextInput:
			text: ''
			font_size: 45
			id: username
		Label:
			text: 'Password'
			font_size: 45
		TextInput:
			text: ''
			font_size: 45
			id: password
			password: True
		Button:
			text: 'Login'
			font_size: 45
			on_press: root.verify()
		Label:
			font_size: 45
		Button:
			text: 'Exit'
			font_size: 45
			on_press: root.dismiss()

<MainScreen>:	
	label_wid: this_name
	bill_wid: this_bill
	input_wid: this_meter
	# previous_wid: this_previous
	# input_read: this_reading
	# consumption_wid: this_consumption
	date_wid: this_date
	BoxLayout:
		orientation: 'vertical'
		GridLayout:
			cols: 2
			Label:
				text: 'Billing'		
				background_color: 1, 1, 1, 1
				font_size: 40
			Label:
				text: 'Statement'
				font_size: 40
			Label:
				text: 'Date'		
				font_size: 30
			Label:
				text: ''		
				font_size: 30
				id: this_date
			Label:
				text: 'Meter Number'		
				font_size: 30
			TextInput:
				text: ''		
				font_size: 30
				id: this_meter
			Button:
				text: 'Search'
				font_size: 30
				on_press: root.searchDB()
			Label:
				font_size: 30
			Label:
				text: 'Billing Number'		
				font_size: 30
			Label:
				text: ''		
				font_size: 30
				id: this_bill
			Label:
				text: 'Name'		
				font_size: 30
			Label:
				text: ''		
				font_size: 30
				id: this_name
			Label:
				text: 'Previous Reading'		
				font_size: 30
			Label:
				text: ''		
				font_size: 30
				id: this_previous
			Label:
				text: 'Current Reading'		
				font_size: 30
			TextInput:
				text: ''		
				font_size: 30
				id: this_reading
			Button:
				text: 'Compute'
				font_size: 30
				on_press: root.computer()
			Label:
				font_size: 30
			Label:
				text: 'Consumption'		
				font_size: 30
			Label:
				text: ''		
				font_size: 30
				id: this_consumption
			Label:
				text: 'Amount Due'		
				font_size: 30
			Label:
				text: ''		
				font_size: 30
				id: this_due
			Button:
				text: 'Save'
				font_size: 30
				on_press: root.saveDB()
			Button:
				text: 'Back'
				font_size: 30
				on_press: root.manager.current = 'homescreen'

<PopupName>:
	title: 'San Pascual Waterworks'
	auto_dismiss: False
	size_hint: .4, .2
	Button:
		text: 'Transaction saved!'
		on_release: root.dismiss()

<LoginMessage>:
	title: 'San Pascual Waterworks'
	auto_dismiss: False
	size_hint: .4, .2
	Button:
		text: 'Wrong username or password.'
		on_release: root.dismiss()

<ErrorMessage>:
	title: 'San Pascual Waterworks'
	auto_dismiss: False
	size_hint: .4, .2
	Button:
		text: 'Enter Current Reading.'
		on_release: root.dismiss()

<SearchMessage>:
	title: 'San Pascual Waterworks'
	auto_dismiss: False
	size_hint: .4, .2
	Button:
		text: 'Enter Meter Number.'
		on_release: root.dismiss()

<GreaterMessage>:
	title: 'San Pascual Waterworks'
	auto_dismiss: False
	size_hint: .4, .2
	Button:
		text: 'Invalid Input.'
		on_release: root.dismiss()

""")




# Declare both screens
class GreaterMessage(Popup):
	pass

class SearchMessage(Popup):
	pass

class LoginMessage(Popup):
	pass

class PopupName(Popup):
	pass

class ErrorMessage(Popup):
	pass

class HomeScreen(Screen):
		def verify(self):
				if self.ids["username"].text == "admin" and self.ids["password"].text == "admin":
						self.manager.current = "mainscreen"
				else:
						LoginMessage().open()


class MainScreen(Screen):
	def searchDB(self):
		self.this_name = str()
		self.this_meter = str()
		self.this_bill = str()
		self.this_previous = str()
		self.input_read = str()
		self.consumption_wid = str()

		self.this_date = str()

		now = datetime.now()
		strg = now.strftime('%B %d, %Y')

		self.date_wid.text = str(strg)

		meter = self.input_wid.text

		if meter == '':
			SearchMessage().open()
		else:

			conn = sqlite3.connect('sanpascualww.db')

			c = conn.cursor()

			# Select Clients
			c.execute("SELECT * FROM clients WHERE meterNumber = " + '"' + (str(meter))  + '"')

			rows = c.fetchall()

			for row in rows:
				# row = [str(item[1]) for item in c.fetchall()]
				self.label_wid.text = str(row[1])

			# Output Billing Counter
			c.execute("SELECT * FROM billing")

			rows = c.fetchall()

			for row in rows:
				add = int(str(row[0])) + 1
				self.bill_wid.text = str(add)

			# Output Billing First
			c.execute("SELECT * FROM billing_first WHERE meterNumber = " + '"' + (str(meter))  + '"')

			rows = c.fetchall()

			for row in rows:
				self.ids.this_previous.text = str(row[2])

	def computer(self):
		meter = self.input_wid.text

		previous = self.ids.this_previous.text
		present = self.ids.this_reading.text
	
		conn = sqlite3.connect('sanpascualww.db')

		c = conn.cursor()

		c.execute("SELECT * FROM clients WHERE meterNumber = " + '"' + (str(meter))  + '"')

		rows = c.fetchall()

		if present == '':
			ErrorMessage().open()

		else:
			if int(present) <= int(previous):
				GreaterMessage().open()
			else:
				self.ids.this_consumption.text = str(int(present) - int(previous))
				consumption = self.ids.this_consumption.text
				for category in rows:
					if (str(category[4])) == "Residential":
						if int(consumption) <= 10:
											self.ids.this_due.text = str(int(130))
						if int(consumption) == 11:
											self.ids.this_due.text = str(int(147))
						if int(consumption) == 12:
											self.ids.this_due.text = str(int(164))
						if int(consumption) == 13:
											self.ids.this_due.text = str(int(181))
						if int(consumption) == 14:
											self.ids.this_due.text = str(int(130))
						if int(consumption) == 15:
											self.ids.this_due.text = str(int(198))
						if int(consumption) == 16:
											self.ids.this_due.text = str(int(215))
						if int(consumption) == 17:
											self.ids.this_due.text = str(int(232))

					if (str(category[4])) == "Commercial":
						if int(consumption) <= 10:
											self.ids.this_due.text = str(int(180))
						if int(consumption) == 11:
											self.ids.this_due.text = str(int(200))
						if int(consumption) == 12:
											self.ids.this_due.text = str(int(220))
						if int(consumption) == 13:
											self.ids.this_due.text = str(int(240))
						if int(consumption) == 14:
											self.ids.this_due.text = str(int(260))
						if int(consumption) == 15:
											self.ids.this_due.text = str(int(280))
						if int(consumption) == 16:
											self.ids.this_due.text = str(int(300))
						if int(consumption) == 17:
											self.ids.this_due.text = str(int(320))

			

	def saveDB(self):
		now = datetime.now()
		month = now.strftime('%B')
		day = now.strftime('%d')
		year = now.strftime('%Y')

		bill = self.ids.this_bill.text
		meter = self.ids.this_meter.text
		consumption = self.ids.this_consumption.text
		due = self.ids.this_due.text
		previous = self.ids.this_previous.text
		present = self.ids.this_reading.text 

		conn = sqlite3.connect('sanpascualww.db')

		c = conn.cursor()
		c2 = conn.cursor()

		sql = "INSERT INTO billing (BillingNumber, meterNumber, Consumption, BillingMonth, Year, AmountDue, Paid) VALUES (?, ?, ?, ?, ?, ?, ?)"
		c.execute(sql, (str(bill), str(meter), str(consumption), str(month), int(year), str(due), str("No")))

		sql2 = "INSERT INTO billling_counter (BillingNumber, id) VALUES (?, ?)"
		c2.execute(sql2, (str(bill), (int(1))))

		sql3 = "INSERT INTO billing_first (meterNumber, recent_billing, new_billing, Month, Year) VALUES (?, ?, ?, ?, ?)"
		c.execute(sql3, (str(meter), str(previous), str(present), str(month), int(year)))

		# c.execute("SELECT * from billing WHERE BillingNumber  = " + '"' + (str(bill))  + '"')
		# data = c.fetchall()

		# for count in data:
		# 		due = str(count[5])
		# 		bill_month = str(count[3])

		# c.execute("SELECT * from clients WHERE meterNumber  = " + '"' + (str(meter))  + '"')
		# num = c.fetchall()

		# for number in num:
		# 		phone = int(str(number[2]))
		# 		client_name = str(number[1])   

		# account_sid = 'ACe9702fef202e3c9ce9326508fb225270'
		# auth_token = '692f559f62cd5fe3d32194fc501c0117'
		# client = Client(account_sid, auth_token)

		# message = client.messages.create(
		# 		body="Good day, " + str(client_name) + ". This is your bill, " 
		# 						+ str(due) + ".00 for the billing month of " + str(bill_month)
		# 						+ ". Please pay your bill before deadline. Thank you.",
		# 		from_='+18649202934',
		# 		to="+63" +  str(phone)
		# 				)

		conn.commit()
		conn.close()

		PopupName().open()

		self.ids.this_date.text = ""
		self.ids.this_meter.text = ""
		self.ids.this_bill.text = ""
		self.ids.this_name.text = ""
		self.ids.this_reading.text = ""
		self.ids.this_due.text = ""
		self.ids.this_previous.text = ""
		self.ids.this_consumption.text = ""


# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name="homescreen"))
sm.add_widget(MainScreen(name="mainscreen"))



class TestApp(App):

    def build(self):
	    
        return sm

if __name__ == '__main__':
    TestApp().run()