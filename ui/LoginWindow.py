from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
import time
from ui.Helpers import clear_window,get_handcursor

from model.Database import *
from model.Person import *

def logIn_screen(window):
	clear_window(window)
	academy_logo = Image.open("images/diemen_logo2.png")
	academy_logo = academy_logo.resize((350,250), Image.ANTIALIAS)
	test = ImageTk.PhotoImage(academy_logo)
	label_logo = Label(image=test)
	label_logo.image = test
	label_logo.place(x=80,y=0)

	username = StringVar()
	password = StringVar()

	def input_value():
		user_name = username.get()
		pass_word = password.get()
		if type(user_name) == str and user_name != "": #actually this part goes to the db to check username/password
			print("Username: " + user_name) #its temporary for testing only

			#this is the ephemeral encryption for testing the login part, when the db is completed, it will be removed.
			#pass_word = bytes(pass_word, "utf-8")
			#key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
			#cipher_suite = Fernet(key)
			#ciphered_text = cipher_suite.encrypt(pass_word)
			#print("Password: " )
			#print(ciphered_text)

			person = Person()
			if person.loadByUsername(user_name, pass_word):
				is_student = person.getStudent()
				if is_student != None:
					window.open_student(is_student, person, window)
					return

				is_teacher = person.getTeacher()
				is_admin = person.getAdmin()
				if is_teacher != None:
					if is_admin != None:
						window.open_select_role(is_teacher, person,window)
					else:
						window.open_teacher(is_teacher, person,window)
					return

				if is_admin != None:
					window.open_admin(window)
					return

		messagebox.showerror("Invalid input", "Incorrect Username/Password")

	username_label = Label(window, text = 'Username',font="Arial 10 bold")
	username_entry = Entry(window,textvariable = username, font="Arial 10")
	username_label.place(x = 130, y = 180)
	username_entry.place(x=207, y = 180)
	password_label = Label(window, text = 'Password', font="Arial 10 bold")
	password_entry = Entry(window,textvariable = password, font="Arial 10", show = "*")
	password_label.place(x = 130, y = 200)
	password_entry.place(x =207, y = 200)
	submit_button = Button(window,text = "Log In", command = input_value, cursor = get_handcursor())
	submit_button.place(x = 220, y = 300)
