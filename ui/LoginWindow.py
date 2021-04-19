from tkinter import *
from tkinter import Button,GROOVE
from tkinter import messagebox
from PIL import ImageTk, Image  
import time
window_width = 500
window_height = 500
master = Tk()
master.title("Diemen Academy")
master.geometry("500x500")
master.resizable(0, 0)

def clear_window(window):
	window.configure(background="white") 
	for child in window.winfo_children():
		child.destroy()


def loading_screen(window):
	clear_window(window)
	window.configure(background="#006386")
	academy_logo = Image.open("Downloads/diemen_academy.png")
	logo = ImageTk.PhotoImage(academy_logo)
	label_logo = Label(window, image=logo)
	label_logo.place(x=150,y=120)
	window.update()
	time.sleep(3)
	logIn_screen(window)

def logIn_screen(window):
	clear_window(window)
	academy_logo = Image.open("Downloads/diemen_logo2.png")
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
		if type(user_name) != str and user_name != "": #actually this part goes to the db to check username/password
			print("Username: " + user_name)
			print("Password: " + pass_word)
		else:
			messagebox.showerror("Invalid input", "Incorrect Username/Password")
		
	username_label = Label(master, text = 'Username', font=('Courier',14, 'normal'))
	username_entry = Entry(master,textvariable = username, font=('Courier',10,'normal'))
	username_label.place(x = 133, y = 180)
	username_entry.place(x=207, y = 180)
	password_label = Label(master, text = 'Password', font = ('Courier',14,'normal'))
	password_entry = Entry(master,textvariable = password, font=('Courier',10,'normal'), show = "*")
	password_label.place(x = 133, y = 200)
	password_entry.place(x =207, y = 200)
	submit_button = Button(master,text = "Log In", command = input_value)
	submit_button.place(x = 200, y = 250)
	

loading_screen(master)

master.mainloop()
