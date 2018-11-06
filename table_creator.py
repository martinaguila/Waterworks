import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
import random
import time
from kivy.properties import StringProperty
# import psycopg2
import sqlite3
import json
from kivy.uix.label import Label
import pandas

Builder.load_string("""
<HomeScreen>:
	BoxLayout:
		orientation: 'vertical'
		Label:
			text: 'Table Creator'		
			font_size: 45
		Button:
			text: 'Billing Table'
			font_size: 45
			on_press: root.billing()
		Button:
			text: 'BillingFirst Table'
			font_size: 45
			on_press: root.billingFirst()
		Button:
			text: 'BillingCounter Table'
			font_size: 45
            on_press: root.billingCounter()
    # Button:
		# 	text: 'Clients Table'
		# 	font_size: 45
    #   on_press: root.clients()
    # Label:
    #         font_size: 45
    
""")




# Declare both screens
class HomeScreen(Screen):
  def billing(self):

      conn = sqlite3.connect('sanpascualww.db')

      c = conn.cursor()
# Drop table
      c.execute('''DROP TABLE billing
                  
                ''')
    #   c.execute('''DROP TABLE billling_counter
                  
    #             ''')
    
    #   c.execute('''DROP TABLE billing_first
                  
    #             ''')
    #   c.execute('''DROP TABLE clients
                  
    #             ''')

    #   Create table
      c.execute('''CREATE TABLE billing
                  (BillingNumber integer PRIMARY KEY, 
                  meterNumber text, 
                  Consumption integer, 
                  BillingMonth text,
                  Year integer,  
                  AmountDue integer,
                  Paid text
                  )
                ''')

      c.execute("""INSERT INTO billing (BillingNumber, meterNumber, Consumption, BillingMonth, Year, AmountDue, Paid) VALUES (1000, 1, 1, "none", 1900, 1, "none")""")

      conn.commit()
      conn.close()

      # conn = qlite3.connect('sanpascualww.db')
      # cursor = conn.cursor()
      # wakoko = """INSERT INTO stocks (date, trans, symbol, qty, price) VALUES (%s, %s, %s, %s, %s)"""
      # with open('output.csv', 'r') as f:
      #     csv_data = csv.reader(f)
      #     for row in csv_data:
      #         cursor.execute(wakoko, row)
      #         conn.commit()

      # cursor.close()
      # conn.close()

      # csv_data = csv.reader(file('output.csv'))
      # for row in csv_data:
      #     print(row)
      #     wakoko = cursor.execute("""INSERT INTO stocks (date, trans, symbol, qty, price) VALUES ("%s", "%s", "%s", "%s", "%s")""")
      #     cursor.execute(wakoko)
      #     #close the connection to the database.
      #     conn.commit()
      #     conn.close()
      #     print "Done"
  
  def billingFirst(self):

      conn = sqlite3.connect('sanpascualww.db')

      c = conn.cursor()

      c.execute('''DROP TABLE billing_first
                  
                ''')

      # Create table
      c.execute('''CREATE TABLE billing_first
                  (meterNumber text, 
                  recent_billing integer, 
                  new_billing integer, 
                  id integer PRIMARY KEY ON CONFLICT REPLACE)
                ''')

      c.execute("""INSERT INTO billing_first (meterNumber, recent_billing, new_billing) VALUES (1000, 0, 0)""")

      conn.commit()
      conn.close()

  def billingCounter(self):

      conn = sqlite3.connect('sanpascualww.db')

      c = conn.cursor()

      # Create table
      # c.execute('''CREATE TABLE billing_counter
      #             (id integer PRIMARY KEY, 
      #             BillingNumber integer)
      #           ''')

      c.execute('''CREATE TABLE clients
                  (meterNumber integer, 
                  Name text,
                  Phone integer,
                  Address text,
                  Category text,
                  id integer PRIMARY KEY ON CONFLICT REPLACE)
                ''')

      conn.commit()
      conn.close()

  def clients(self):

      conn = sqlite3.connect('sanpascualww.db')

      c = conn.cursor()

      # Create table
    #   c.execute('''CREATE TABLE clients
    #               (meterNumber text, 
    #               Name text,
    #               Phone text,
    #               Address text,
    #               Category text,
    #               id integer PRIMARY KEY)
    #             ''')
    
    #   c.execute('''CREATE TABLE billling_counter
    #             (id integer PRIMARY KEY, 
    #             BillingNumber integer)
    #         ''')

      conn.commit()
      conn.close()

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name="homescreen"))


class TestApp(App):

    def build(self):
	    
        return sm

if __name__ == '__main__':
    TestApp().run()