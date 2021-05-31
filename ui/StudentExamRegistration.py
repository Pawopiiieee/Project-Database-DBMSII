from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial



def student_exam_registration(window, return_function, student): 
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Exam Registration", fg = "#EBEBE9", font = "Arial 24", bg ="#006386")
	header_label.place(x = 120, y = 15)

	courses = student.getEnrolledCourses()
	
	buttons = []
	def confirm_register(exam_n):
		button = buttons[exam_n]
		if button["text"] == "Register":
			button["text"] = "Deregister"
			button["fg"] = "red"

		else:
			button["text"] = "Register"
			button["fg"] = "#1f3d7a"

	exam_pos_y = 200
	exam_number = 0
	for exam in courses:
		exam_label = Label(window,text = exam.coursetitle, fg = "#00293c", font = "Arial 12", bg = "#e6f2ff", highlightbackground ="#8AA989", width = 20)
		exam_label.place(x = 50, y = exam_pos_y,height=30)
		exam_register = Button(window, text = "Register", fg = "#1f3d7a", font = "Arial 12", width = 10, highlightbackground ="#8AA989", command = partial(confirm_register, exam_number))
		exam_register.place(x = 300, y = exam_pos_y,height=30)
		buttons.append(exam_register)
		exam_pos_y += 40
		exam_number += 1

	go_back(window, return_function)
	sign_out(window)