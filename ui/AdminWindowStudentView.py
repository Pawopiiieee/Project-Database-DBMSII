from tkinter import *
from tkinter import ttk
from ui.AdminWindowStudentEnrolledCourses import enrolledCourses_students
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from functools import partial

def student_view(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Student Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 120, y = 15)

	lastname_label = Label(window,text = "Lastname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	lastname_label.place(x = 20, y = 100)

	firstname_label = Label(window,text = "Firstname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	firstname_label.place(x = 250, y = 100)

	studentID_label = Label(window,text = "Student ID", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	studentID_label.place(x = 20, y = 120)

	startYear_label = Label(window,text = "Start Year", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	startYear_label.place(x = 250, y = 120)

	study_label = Label(window,text = "Study", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	study_label.place(x = 20, y = 140)

	studentCounsellor_label = Label(window,text = "Student Counsellor", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	studentCounsellor_label.place(x = 20, y = 160)

	personal_label = Label(window,text = "Personal Detail", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	personal_label.place(x = 20, y = 210)

	dob_label = Label(window,text = "Date of Birth", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	dob_label.place(x = 20, y = 240)

	nationality_label = Label(window,text = "Nationality", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	nationality_label.place(x = 20, y = 260)

	gender_label = Label(window,text = "Gender", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	gender_label.place(x = 20, y = 280)

	address_label = Label(window,text = "Address", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	address_label.place(x = 20, y = 300)

	address_label = Label(window,text = "Address", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	address_label.place(x = 20, y = 320)

	Contact_label = Label(window,text = "Contact", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	Contact_label.place(x = 20, y = 370)

	phoneNumber_label = Label(window,text = "Phone Number", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	phoneNumber_label.place(x = 20, y = 400)

	email_label = Label(window,text = "Email", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	email_label.place(x = 20, y = 420)

	enrollCourses_button = Button(window, text = "View Enrolled Courses",fg = "#00ace6", font="Arial 10 bold",height = 2, width = 18, cursor = get_handcursor(), command = partial(enrolledCourses_students,window, return_function))
	enrollCourses_button.place(x = 160, y = 500)

	go_back(window, return_function)
	sign_out(window)