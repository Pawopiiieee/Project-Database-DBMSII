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

	code_label = Label(window,text = "Code", fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2,width = 12,borderwidth=2, relief="groove")
	code_label.place(x = 35, y = 200)
	subject_label = Label(window,text = "Subject", fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2,width = 22,borderwidth=2, relief="groove")
	subject_label.place(x = 148, y = 200)
	exam_label = Label(window,text = "Exam", fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2,width = 12,borderwidth=2, relief="groove")
	exam_label.place(x = 350, y = 200)

	id_pos_y = 236
	courses_ids = [
		"abc123",
		"def456"
	]
	
	for course_id in courses_ids:
		courseID_label = Label(window,text = course_id, fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2, width = 12,borderwidth=2, relief="groove")
		courseID_label.place(x = 35, y = id_pos_y)
		id_pos_y += 32

	
	subjects = ["acb",
	"edf"
	]
	id_pos_y = 236
	for subject in subjects:
		subject_label = Label(window,text = subject, fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2, width = 22,borderwidth=2, relief="groove")
		subject_label.place(x = 148, y = id_pos_y)
		id_pos_y += 32
	
	id_pos_y = 236
	exam_dates = ["dd/mm/yyyy",
	"dd/mm/yyyy",  
	]
	
	for exam_date in exam_dates:
		subject_label = Label(window,text = exam_date, fg = "#00293c", font = "Courier 15", highlightbackground ="#acd0c0", height = 2, width = 12,borderwidth=2, relief="groove")
		subject_label.place(x = 350, y = id_pos_y)
		id_pos_y += 32





	go_back(window, return_function)
	sign_out(window)