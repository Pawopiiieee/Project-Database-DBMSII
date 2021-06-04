from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out


def personal_data(window, return_function,teacher,person): #this is going to show personal data
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	upper_window.create_rectangle(0, 0, 500,120, fill="#006386",outline = "#006386")

	profile_pic = Image.open("images/removed.png")
	profile_pic = profile_pic.resize((70,70), Image.ANTIALIAS)
	personal_image =ImageTk.PhotoImage(profile_pic)
	personal_image.icon = personal_image
	personal_image_button  = Button(window, image = personal_image)
	personal_image_button.place(x=50, y=30)
	upper_window.create_text(270, 70, fill = "white", font = "Arial 18", text = "Hi! Teacher... ")
	upper_window_label = Label(window,text = "Profile",fg = "#00293c", font = "Impact 24", bg ="#EBEBE9")
	upper_window_label.place(x = 40, y = 125)
	upper_window.pack()

	name_label = Label(window, text = "Name:  ",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	name_label.place(x = 20, y = 180)
	name_label = Label(window, text = (str(person.lname) + "  " + str(person.fname)),fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	name_label.place(x = 120, y = 180)
	dob_label = Label(window, text = "Date of Birth:  ",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	dob_label.place(x= 20, y = 210)
	dob = Label(window, text = person.birthday,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	dob.place(x= 120, y = 210)
	address_label = Label(window, text = "Residential Address:  ",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address_label.place(x= 20, y = 240)
	address = Label(window, text = (str(person.streetname) + " " + str(person.streetNumber)),fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address.place(x= 140, y = 240)
	address_label2 = Label(window, text = "Residential Address:  ",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address_label2.place(x= 20, y = 270)
	address = Label(window, text = (str(person.postalCode) + " " + str(person.city)),fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address.place(x= 140, y = 270)
	diemenID_label = Label(window, text = "Teacher ID: ",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenID_label.place(x= 20, y = 300)
	diemenID = Label(window, text = teacher.teacherID,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenID.place(x= 140, y = 300)
	diemenEmail_label = Label(window, text = "Email:  ",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenEmail_label.place(x= 20, y = 330)
	diemenEmail = Label(window, text = person.email,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenEmail.place(x= 140, y = 330)

	go_back(window, return_function)
	sign_out(window)