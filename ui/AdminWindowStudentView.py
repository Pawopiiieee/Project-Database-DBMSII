from tkinter import *
from tkinter import ttk
from ui.AdminWindowStudentEnrolledCourses import enrolledCourses_students
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from functools import partial
from model import Student,Person

def student_view(window, return_function, student, person):
	clear_window(window)

	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Student Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 120, y = 15)

	lastname_label = Label(window,text = "Lastname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	lastname_label.place(x = 20, y = 100)

	lastname_info = Label(window,text =person.lname, fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	lastname_info.place(x = 140, y = 100)

	firstname_label = Label(window,text = "Firstname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	firstname_label.place(x = 250, y = 100)

	firstname_info = Label(window,text =person.fname , fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	firstname_info.place(x = 350, y = 100)

	studentID_label = Label(window,text = "Student ID", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	studentID_label.place(x = 20, y = 120)

	studentID_info = Label(window,text =student.studentID, fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	studentID_info.place(x = 140, y = 120)

	startYear_label = Label(window,text = "Start Year", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	startYear_label.place(x = 250, y = 120)

	startYear_info = Label(window,text =student.startYear , fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	startYear_info.place(x = 350, y = 120)

	study_label = Label(window,text = "Study", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	study_label.place(x = 20, y = 140)

	study_info = Label(window,text = student.enrolled , fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	study_info.place(x = 140, y = 140)


	studentCounsellor_label = Label(window,text = "Student Counsellor", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	studentCounsellor_label.place(x = 20, y = 160)

	councelor = student.getStudentCounsellor()
	councelperson = councelor.getPerson()

	studentCounsellor_info = Label(window,text = (councelperson.fname + " " + councelperson.lname), fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	studentCounsellor_info.place(x = 160, y = 160)

	personal_label = Label(window,text = "Personal Detail", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	personal_label.place(x = 20, y = 210)

	dob_label = Label(window,text = "Date of Birth", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	dob_label.place(x = 20, y = 240)

	dob_info = Label(window,text =person.birthday, fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	dob_info.place(x = 140, y = 240)

	nationality_label = Label(window,text = "Nationality", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	nationality_label.place(x = 20, y = 260)

	nationality_info = Label(window,text =person.nationality , fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	nationality_info.place(x = 140, y = 260)

	gender_label = Label(window,text = "Gender", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	gender_label.place(x = 20, y = 280)

	gender_info = Label(window,text =person.gender, fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	gender_info.place(x = 140, y = 280)

	address_label = Label(window,text = "Address", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	address_label.place(x = 20, y = 300)

	address_info = Label(window,text = (str(person.streetname) + " " + str(person.streetNumber)), fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	address_info.place(x = 140, y = 300)

	address2_label = Label(window,text = "Address", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	address2_label.place(x = 20, y = 320)

	address2_info = Label(window,text = (str(person.postalCode) + " " + str(person.city)), fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	address2_info.place(x = 140, y = 320)

	Contact_label = Label(window,text = "Contact", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	Contact_label.place(x = 20, y = 370)

	phoneNumber_label = Label(window,text = "Phone Number", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	phoneNumber_label.place(x = 20, y = 400)

	phoneNumber_info = Label(window,text =person.phone , fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	phoneNumber_info.place(x = 140, y = 400)

	email_label = Label(window,text = "Email", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	email_label.place(x = 20, y = 420)

	email_info = Label(window,text = person.email, fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	email_info.place(x = 140, y = 420)

	enrollCourses_button = Button(window, text = "View Enrolled Courses",fg = "#00ace6", font="Arial 10 bold",height = 2, width = 18, cursor = get_handcursor(), command = partial(enrolledCourses_students,window, return_function, student))
	enrollCourses_button.place(x = 160, y = 500)

	go_back(window, return_function)
	sign_out(window)