from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window

def sign_out(window):
	def call_sign_in_window():
		window.open_login(window)
	signOut_icon = ImageTk.PhotoImage(file="images/signOut.png")
	
	signOut_button = Button(window, image = signOut_icon, command = call_sign_in_window, cursor = "hand")
	signOut_button.icon = signOut_icon
	signOut_button.place(x=400, y = 650)