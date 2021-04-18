from tkinter import *
from tkinter import Button,GROOVE
from tkinter import messagebox
from PIL import ImageTk, Image  

window_width = 500
window_height = 500
master = Tk()
master.title("Inholland Academy")
master.geometry("500x500")
master.resizable(0, 0)
#master.configure(background="#132A40") 


academy_logo = Image.open("Downloads/inholland_logo.png")
academy_logo = academy_logo.resize((300,80), Image.ANTIALIAS)
test = ImageTk.PhotoImage(academy_logo)
label_logo = Label(image=test)
label_logo.image = test
label_logo.place(x=100,y=25)

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
username_label.place(x = 133, y = 150)
username_entry.place(x=207, y = 150)
password_label = Label(master, text = 'Password', font = ('Courier',14,'normal'))
password_entry = Entry(master,textvariable = password, font=('Courier',10,'normal'), show = "*")
password_label.place(x = 133, y = 170)
password_entry.place(x =207, y = 170)
submit_button = Button(master,text = "Log In", command = input_value)
submit_button.place(x = 200, y = 250)

master.mainloop()
