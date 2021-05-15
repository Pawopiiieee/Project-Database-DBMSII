from tkinter import *
from tkinter import ttk 
from ui.AdminWindowStudyViewStudents import view_students
from ui.AdminWindowStudyViewCourses import view_courses
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial

def study_over_view(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window,text = "Title", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)

	desc_label = Label(window,text = "Description", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	desc_label.place(x = 20, y = 130)

	language_label = Label(window,text = "Language", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	language_label.place(x = 20, y = 350)	

	startYear_label = Label(window,text = "Start Year", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	startYear_label.place(x = 20, y = 380)

	duration_label = Label(window,text = "Duration", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	duration_label.place(x = 20, y = 410)

	student_button = Button(window, text = "Student Lists",fg = "#00ace6", font="Alice 18 bold",height = 2, width = 13, cursor = "pointinghand",command = partial(view_students, window, return_function))
	student_button.place(x = 50, y = 470)

	course_button = Button(window, text = "Course Lists",fg = "#F39C12", font="Alice 18 bold",height = 2, width = 13, cursor = "pointinghand",command = partial(view_courses, window, return_function))
	course_button.place(x = 300, y = 470)

	go_back(window, return_function)
	sign_out(window)