from tkinter import *
from ui.AdminWindowTeacherViewTeach import teaching_courses
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial

def teacher_view(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Teacher Overview", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 120, y = 15)

	lastname_label = Label(window,text = "Lastname", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	lastname_label.place(x = 20, y = 100)

	firstname_label = Label(window,text = "Firstname", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	firstname_label.place(x = 250, y = 100)

	teacherID_label = Label(window,text = "Teacher ID", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	teacherID_label.place(x = 20, y = 120)

	salary_label = Label(window,text = "Salary", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	salary_label.place(x = 250, y = 120)

	studentCounsellor_label = Label(window,text = "Student Counsellor", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	studentCounsellor_label.place(x = 20, y = 140)

	personal_label = Label(window,text = "Personal Detail", fg = "#006386", font = "Alice 18 bold", bg ="#EBEBE9")
	personal_label.place(x = 20, y = 210)

	dob_label = Label(window,text = "Date of Birth", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	dob_label.place(x = 20, y = 240)

	nationality_label = Label(window,text = "Nationality", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	nationality_label.place(x = 20, y = 260)

	gender_label = Label(window,text = "Gender", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	gender_label.place(x = 20, y = 280)

	address_label = Label(window,text = "Address", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	address_label.place(x = 20, y = 300)

	address_label = Label(window,text = "Address", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	address_label.place(x = 20, y = 320)

	Contact_label = Label(window,text = "Contact", fg = "#006386", font = "Alice 18 bold", bg ="#EBEBE9")
	Contact_label.place(x = 20, y = 370)

	phoneNumber_label = Label(window,text = "Phone Number", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	phoneNumber_label.place(x = 20, y = 400)

	email_label = Label(window,text = "Email", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	email_label.place(x = 20, y = 420)

	teachingCourses_button = Button(window, text = "View Teaching Courses",fg = "#00ace6", font="Alice 16 bold",height = 2, width = 18, cursor = "pointinghand", command = partial(teaching_courses,window, return_function))
	teachingCourses_button.place(x = 160, y = 500)

	go_back(window, return_function)
	sign_out(window)