from tkinter import *
from tkinter import ttk
from ui.Helpers import clear_window, go_back,get_handcursor
import ui.AdminWindowStudentEnrolledCourses
from tkinter.messagebox import askquestion,showerror,showinfo
from ui.SignOut import sign_out

from model.Course import *

def view_courses_add(window, return_function,student):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window,text = "Course", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)

	selected_course = StringVar()
	study = student.getStudy()
	courses = study.getCoursesInStudy()
	coursenames = []
	for c in courses:
		coursenames.append(c.coursetitle)

	course_ch = ttk.Combobox(window,textvariable = selected_course,width = 20)
	course_ch["value"] = coursenames
	course_ch["state"] = "readonly"
	def course_changed (event):
		confirm_msg = f"You Selected {course_ch.get()}!"
		showinfo(title="Result", message= confirm_msg)
	course_ch.bind("<<ComboboxSelected>>", course_changed)
	course_ch.place(x = 100, y = 100)


	def submit_data():
		get_course = selected_course.get()
		
		result = askquestion(title="Confirmation", message= "Do you want to proceed?")
		if result == "yes":
			course_idx = coursenames.index(get_course)
			student.enrollInCourse(courses[course_idx].courseID)
			ui.AdminWindowStudentEnrolledCourses.enrolledCourses_students(window, return_function, student)

	submit_text = Button(window, text = "Submit",font = "Arial 14 bold",fg = "#006386",bg="#48C9B0",highlightbackground ="#48C9B0",command =submit_data,cursor = get_handcursor())
	submit_text.place(x=180, y = 300, width = 150,height = 30)


	go_back(window, return_function)
	sign_out(window)