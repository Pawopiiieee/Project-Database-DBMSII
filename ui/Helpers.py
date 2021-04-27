from PIL import ImageTk
from tkinter import Button

def clear_window(window):
	window.configure(background="white") 
	for child in window.winfo_children():
		child.destroy()


def go_back(window, return_function):
	def call_go_back():
		return_function(window)
	home_icon = ImageTk.PhotoImage(file="images/home.png")
	
	go_back_button = Button(window, image = home_icon, command = call_go_back, cursor = "hand")
	go_back_button.icon = home_icon
	go_back_button.place(x=50, y = 650)