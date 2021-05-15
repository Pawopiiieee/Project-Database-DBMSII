from tkinter import *
from tkinter import ttk 
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out

def enrolledCourses_students(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Student Overview", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 140, y = 15)

	student_name_label = Label(window, text = "StudentName", fg = "#006386", font="Alice 13 bold",bg = "#EBEBE9")
	student_name_label.place(x=20, y = 100)
	student_id_label = Label(window, text = "Student ID", fg = "#006386", font="Alice 13 bold",bg = "#EBEBE9")
	student_id_label.place(x=20, y = 130)	
	Study_label = Label(window, text = "Study",fg = "#006386", font="Alice 13 bold",bg = "#EBEBE9")
	Study_label.place(x=20, y = 160)

	Courses_label = Label(window, text = "Course Name",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 25,bg ="#006386")
	Courses_label.place(x=20, y = 220)

	CourseID_label = Label(window, text = "Course ID",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 13,bg ="#006386")
	CourseID_label.place(x=250, y = 220)

	grades_label = Label(window, text = "Grade",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 10,bg ="#006386")
	grades_label.place(x=370, y = 220)

	courses = ["abc","def","ghi","jkl","mno"]
	course_id= ["AA12345","AA22345","AA32345","AA42345","AA52345"]
	num_pos_y = 250
	
	for i in range (len(courses)):

		lastName_label = Label(window, text = courses[i],fg = "#00293c", font = "Alice 13", height = 2, width = 25,relief="ridge",borderwidth=2)
		lastName_label.place(x = 20, y = num_pos_y)

		studentID_label = Label(window, text = course_id[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 13,relief="ridge",borderwidth=2)
		studentID_label.place(x = 250 , y = num_pos_y)

		bg_label = Label(window, height = 2, width = 10,relief="ridge",borderwidth=2)
		bg_label.place(x=370, y= num_pos_y)

		num_pos_y += 30
	

	go_back(window, return_function)
	sign_out(window)
