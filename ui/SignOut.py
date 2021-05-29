from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window,get_handcursor

def sign_out(window):
	def call_sign_in_window():
		window.open_login(window)
	signOut_icon = Image.open("images/Signout.png")
	signOut_icon= signOut_icon.resize((35,35), Image.ANTIALIAS)
	signOut_image =ImageTk.PhotoImage(signOut_icon)
	signOut_image.icon = signOut_image
	signOut_button = Button(window, image = signOut_image,width = 50, height = 50, command = call_sign_in_window, cursor = get_handcursor())
	signOut_button.icon = signOut_icon
	signOut_button.place(x=400, y = 655,width = 50, height = 50)