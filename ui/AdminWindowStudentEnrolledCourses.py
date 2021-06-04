from tkinter import *
from tkinter import ttk
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from ui.AdminWindowStudentEnrolledCoursesAdd import view_courses_add
from functools import partial
from model import Student,Study,Person


def enrolledCourses_students(window, return_function, student):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Student Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 110, y = 15)

	person = student.getPerson()
	student_name_label = Label(window, text = "StudentName", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	student_name_label.place(x=20, y = 100)
	student_name_label = Label(window, text = person.fname + " " + person.lname, fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	student_name_label.place(x=120, y = 100)

	student_id_label = Label(window, text = "Student ID", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	student_id_label.place(x=20, y = 130)
	student_id_label = Label(window, text = student.studentID, fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	student_id_label.place(x=120, y = 130)

	Study_label = Label(window, text = "Study",fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	Study_label.place(x=20, y = 160)
	Study_label = Label(window, text = student.getStudy().studyname,fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	Study_label.place(x=120, y = 160)

	add_course = Button(window,text = "+Add Courses",fg = "#006386", font = "Arial 10 bold", cursor = get_handcursor(),highlightbackground = "#006386",command = partial(view_courses_add, window, return_function, student))
	add_course.place(x = 380, y = 160)

	Courses_label = Label(window, text = "Course Name",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	Courses_label.place(x=20, y = 200,width=290, height=30)

	CourseID_label = Label(window, text = "Course ID",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	CourseID_label.place(x=310, y = 200, width=100, height=30)

	grades_label = Label(window, text = "Grade",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	grades_label.place(x=410, y = 200, width= 70,height=30)

	courses = student.getEnrolledCourses()
	grades = student.getStudentGrades()

	num_pos_y = 230

	for i in range (len(courses)):

		course_label = Label(window, text = courses[i].coursetitle,fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		course_label.place(x=20, y = num_pos_y,width=290, height=30)

		courseID_label = Label(window, text = courses[i].courseID,fg = "#00293c", font = "Arial 10", relief="ridge",borderwidth=2)
		courseID_label.place(x=310, y = num_pos_y, width=100, height=30)

		bg_label = Label(window, relief="ridge",borderwidth=2)
		bg_label.place(x=410, y = num_pos_y, width= 70,height=30)
		num_pos_y += 30

	num_pos_y = 230
	for i in range (len(grades)):
		grade_label = Label(window,text = grades[i].grade,fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		grade_label.place(x=410, y = num_pos_y, width= 70,height=30)

		num_pos_y += 30


	go_back(window, return_function)
	sign_out(window)
