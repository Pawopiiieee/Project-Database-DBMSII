from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out


def student_personal_course(window, return_function): 
	clear_window(window)

	whole_window = Canvas(window, width = 500, height = 700, bg = "#75b1a9")
	whole_window.pack()
	header_label = Label(window,text = "Course Name", fg = "#00293c", font = "Impact 35", bg ="#d9b44a", height = 2, width = 15)
	header_label.place(x = 105, y = 40)

	code_label = Label(window,text = "Code", fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2,width = 14,borderwidth=2, relief="groove")
	code_label.place(x = 35, y = 200)
	subject_label = Label(window,text = "Subject", fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2,width = 22,borderwidth=2, relief="groove")
	subject_label.place(x = 150, y = 200)
	exam_label = Label(window,text = "Exam", fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2,width = 12,borderwidth=2, relief="groove")
	exam_label.place(x = 350, y = 200)



	go_back(window, return_function)
	sign_out(window)