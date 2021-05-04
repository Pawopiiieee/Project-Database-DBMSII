from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial



def student_exam_registration(window, return_function): #this is going to show personal data
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#75b1a9")
	whole_window.pack()
	header_label = Label(window,text = "Exam Registration", fg = "#00293c", font = "Impact 35", bg ="#d9b44a", height = 2, width = 15)
	header_label.place(x = 105, y = 40)

	exams = [
		"exam 1",
		"exam 2"
	]

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
	for exam in exams:
		exam_label = Label(window,text = exam, fg = "#00293c", font = "Impact 15", highlightbackground ="#acd0c0", height = 2, width = 15)
		exam_label.place(x = 50, y = exam_pos_y)
		exam_register = Button(window, text = "Register", fg = "#1f3d7a", font = "Impact 15", height = 2, width = 10, highlightbackground ="#d9b44a", command = partial(confirm_register, exam_number))
		exam_register.place(x = 300, y = exam_pos_y)
		buttons.append(exam_register)
		exam_pos_y += 50
		exam_number += 1

	go_back(window, return_function)
	sign_out(window)