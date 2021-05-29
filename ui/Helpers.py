from PIL import ImageTk
from tkinter import Button
from passlib.context import CryptContext
import sys

def clear_window(window):
	window.configure(background="white")
	for child in window.winfo_children():
		child.destroy()

def get_handcursor():
	if sys.platform == "darwin":
		return "pointinghand"
	else:
		return "hand2"


def go_back(window, return_function):
	def call_go_back():
		return_function(window)
	home_icon = ImageTk.PhotoImage(file="images/home.png")

	go_back_button = Button(window, image = home_icon, width = 50, height = 50, command = call_go_back, cursor = get_handcursor())
	go_back_button.icon = home_icon
	go_back_button.place(x=50, y = 650, width = 50, height = 50)

#this is for checking the password encryption in db
pass_word = CryptContext(schemes=["pbkdf2_sha256"],default="pbkdf2_sha256",pbkdf2_sha256__default_rounds=30000)

def encrypt_password(password):
	return pass_word.encrypt(password)

def check_encrypted_password(password,hashed):
	return pass_word.verify(password,hash)