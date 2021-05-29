from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
import time
from ui.Helpers import clear_window
from ui.LoginWindow import logIn_screen


def loading_screen(window):
	clear_window(window)
	window.configure(background="#006386")
	academy_logo = Image.open("images/diemen_academy.png")
	logo = ImageTk.PhotoImage(academy_logo)
	label_logo = Label(window, image=logo)
	label_logo.place(x=150,y=120)
	window.update()
	time.sleep(3)
	logIn_screen(window)