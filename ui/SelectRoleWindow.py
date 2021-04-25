from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
import time
from ui.Helpers import clear_window

def select_role(window): #the case that a teacher is also an admin 
	clear_window(window)
	
	upper_window = Canvas(window, width = 500)
	upper_window.create_rectangle(0, 0, 500, 70, fill="#006386")
	upper_window.place(x = 0, y = 0)

	academy_logo = Image.open("images/diemen_logo2.png")
	academy_logo = academy_logo.resize((185,150), Image.ANTIALIAS)
	test = ImageTk.PhotoImage(academy_logo)
	label_logo = Label(image=test)
	label_logo.image = test
	label_logo.place(x=170,y=70)


	admin_button = Button(window,text = "Continue as an Admin", bd = '5',command = window.destroy)
	admin_button.place(x = 180, y = 250)
	teacher_button = Button(window,text = "Continue as a Teacher", bd = '5',command = window.destroy)
	teacher_button.place(x = 180, y = 300)