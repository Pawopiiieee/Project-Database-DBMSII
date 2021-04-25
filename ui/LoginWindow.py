from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from cryptography.fernet import Fernet  
import time
from ui.Helpers import clear_window
from ui.SelectRoleWindow import select_role


def logIn_screen(window):
	clear_window(window)
	academy_logo = Image.open("images/diemen_logo2.png")
	academy_logo = academy_logo.resize((350,250), Image.ANTIALIAS)
	test = ImageTk.PhotoImage(academy_logo)
	label_logo = Label(image=test)
	label_logo.image = test
	label_logo.place(x=100,y=0)

	username = StringVar()
	password = StringVar()

	def input_value():
		user_name = username.get()
		pass_word = password.get()
		if type(user_name) == str and user_name != "": #actually this part goes to the db to check username/password
			print("Username: " + user_name) #its temporary for testing only
			pass_word = bytes(pass_word, "utf-8")
			key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
			cipher_suite = Fernet(key)
			ciphered_text = cipher_suite.encrypt(pass_word)
			print("Password: " ) 
			print(ciphered_text)
			if user_name == "test":
				select_role(window)
				return
		messagebox.showerror("Invalid input", "Incorrect Username/Password")
		
	username_label = Label(window, text = 'Username', font=('Courier',14, 'normal'))
	username_entry = Entry(window,textvariable = username, font=('Courier',10,'normal'))
	username_label.place(x = 133, y = 180)
	username_entry.place(x=207, y = 180)
	password_label = Label(window, text = 'Password', font = ('Courier',14,'normal'))
	password_entry = Entry(window,textvariable = password, font=('Courier',10,'normal'), show = "*")
	password_label.place(x = 133, y = 200)
	password_entry.place(x =207, y = 200)
	submit_button = Button(window,text = "Log In", command = input_value)
	submit_button.place(x = 200, y = 250)
	
