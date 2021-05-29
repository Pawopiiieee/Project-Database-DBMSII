from tkinter import *
from tkinter import ttk
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out

def enrolledCourses_students(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Student Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 110, y = 15)

	student_name_label = Label(window, text = "StudentName", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	student_name_label.place(x=20, y = 100)
	student_id_label = Label(window, text = "Student ID", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	student_id_label.place(x=20, y = 130)
	Study_label = Label(window, text = "Study",fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	Study_label.place(x=20, y = 160)

	Courses_label = Label(window, text = "Course Name",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	Courses_label.place(x=20, y = 220,width=250, height=30)

	CourseID_label = Label(window, text = "Course ID",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	CourseID_label.place(x=270, y = 220, width=140, height=30)

	grades_label = Label(window, text = "Grade",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	grades_label.place(x=390, y = 220, width= 90,height=30)

	courses = ["abc","def","ghi","jkl","mno"]
	course_id= ["AA12345","AA22345","AA32345","AA42345","AA52345"]
	num_pos_y = 250

	for i in range (len(courses)):

		course_label = Label(window, text = courses[i],fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		course_label.place(x=20, y = num_pos_y,width=250, height=30)

		courseID_label = Label(window, text = course_id[i],fg = "#00293c", font = "Arial 10", relief="ridge",borderwidth=2)
		courseID_label.place(x=270, y = num_pos_y, width=140, height=30)

		bg_label = Label(window,relief="ridge",borderwidth=2)
		bg_label.place(x=390, y = num_pos_y, width= 90,height=30)

		num_pos_y += 30


	go_back(window, return_function)
	sign_out(window)
