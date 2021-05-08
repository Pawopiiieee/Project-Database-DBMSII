from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out


def student_personal_data(window, return_function): #this is going to show personal data
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	upper_window.create_rectangle(0, 0, 500,120, fill="#006386",outline = "#006386")	

	profile_pic = Image.open("images/hooman.png")
	profile_pic = profile_pic.resize((70,70), Image.ANTIALIAS)
	personal_image =ImageTk.PhotoImage(profile_pic)
	personal_image.icon = personal_image
	personal_image_button  = Button(window, image = personal_image)
	personal_image_button.place(x=50, y=30)
	upper_window.create_text(320, 70, fill = "white", font = "Arial 18", text = "Hi! Legendary Wait_forIt ")
	upper_window_label = Label(window,text = "Profile",fg = "#00293c", font = "Impact 30", bg ="#EBEBE9")
	upper_window_label.place(x = 40, y = 125)
	upper_window.pack()

	name_label = Label(window, text = "Name:  LagendDaily Wait_for_it",fg = "#00293c", font = "Alice 15", bg ="#EBEBE9")
	name_label.place(x = 40, y = 180)
	dob_label = Label(window, text = "Date of Birth:  January 31 1999",fg = "#00293c", font = "Alice 15", bg ="#EBEBE9")
	dob_label.place(x= 40, y = 210)
	address_label = Label(window, text = "Residential Address:  12AB GoldenStraat Amsterdam 1999XY",fg = "#00293c", font = "Alice 15", bg ="#EBEBE9")
	address_label.place(x= 40, y = 210)
	diemenID_label = Label(window, text = "Student ID:  lastname12345",fg = "#00293c", font = "Alice 15", bg ="#EBEBE9")
	diemenID_label.place(x= 40, y = 240)
	diemenEmail_label = Label(window, text = "Email:  lastname@diemenacademy.nl",fg = "#00293c", font = "Alice 15", bg ="#EBEBE9")
	diemenEmail_label.place(x= 40, y = 270)
	study_label = Label(window, text = "Study:  MiddleEarth Magic",fg = "#00293c", font = "Alice 15", bg ="#EBEBE9")
	study_label.place(x= 40, y = 300)

	go_back(window, return_function)
	sign_out(window)
	