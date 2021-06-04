from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from model import Student,Person


def student_personal_data(window, return_function,student,person): #this is going to show personal data
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	upper_window.create_rectangle(0, 0, 500,120, fill="#006386",outline = "#006386")

	profile_pic = Image.open("images/hooman.png")
	profile_pic = profile_pic.resize((70,70), Image.ANTIALIAS)
	personal_image =ImageTk.PhotoImage(profile_pic)
	personal_image.icon = personal_image
	personal_image_button  = Button(window, image = personal_image)
	personal_image_button.place(x=50, y=30)
	upper_window.create_text(200, 70, fill = "white", font = "Arial 12", text = "Hi There!")
	upper_window_label = Label(window,text = "Profile",fg = "#00293c", font = "Impact 30", bg ="#EBEBE9")
	upper_window_label.place(x = 40, y = 125)
	upper_window.pack()

	name = Label(window, text = "Name",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	name.place(x = 20, y = 180)
	name_label = Label(window, text = (str(person.fname) + " " + str(person.lname)),fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	name_label.place(x = 140, y = 180)
	dob_label = Label(window, text = "Date of Birth",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	dob_label.place(x= 20, y = 210)
	dob = Label(window, text = person.birthday,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	dob.place(x= 140, y = 210)
	address_label = Label(window, text = "Address",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address_label.place(x= 20, y = 240)
	address = Label(window, text = (str(person.streetname) + " " + str(person.streetNumber)),fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address.place(x= 140, y = 240)
	address_label = Label(window, text = "Address",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address_label.place(x= 20, y = 270)
	address = Label(window, text = (str(person.postalCode) + " " + str(person.city)),fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	address.place(x= 140, y = 270)
	diemenID_label = Label(window, text = "Student ID",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenID_label.place(x= 20, y = 300)
	diemenID = Label(window, text = student.studentID,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenID.place(x= 140, y = 300)
	diemenEmail_label = Label(window, text = "Email",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenEmail_label.place(x= 20, y = 330)
	diemenEmail = Label(window, text = person.email,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	diemenEmail.place(x= 140, y = 330)
	study_label = Label(window, text = "Study",fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	study_label.place(x= 20, y = 360)
	study = Label(window, text = student.enrolled,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	study.place(x= 140, y = 360)

	go_back(window, return_function)
	sign_out(window)
