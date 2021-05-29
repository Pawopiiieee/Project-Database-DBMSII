from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out


def student_personal_course(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Course Name", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 150, y = 15)



	code_label = Label(window,text = "Course ID", fg = "#00293c", font = "Arial 10", highlightbackground ="#acd0c0", height = 2,width = 12,borderwidth=2, relief="groove")
	code_label.place(x = 30, y = 120,width = 105,height=30)
	subject_label = Label(window,text = "Course Name", fg = "#00293c", font = "Arial 10", highlightbackground ="#acd0c0", height = 2,width = 22,borderwidth=2, relief="groove")
	subject_label.place(x = 135, y = 120,width = 200,height=30)
	exam_label = Label(window,text = "Exam", fg = "#00293c", font = "Arial 10", highlightbackground ="#acd0c0", height = 2,width = 12,borderwidth=2, relief="groove")
	exam_label.place(x = 335, y = 120,width = 150,height=30)

	id_pos_y = 150
	courses_ids = [
		"abc123",
		"def456"
	]

	for course_id in courses_ids:
		courseID_label = Label(window,text = course_id, fg = "#00293c", font = "Arial 10", highlightbackground ="#acd0c0", height = 2, width = 12,borderwidth=2, relief="groove")
		courseID_label.place(x = 30, y = id_pos_y,width = 105,height=30)
		id_pos_y += 30

	id_pos_y = 150
	subjects = ["acb",
	"edf"
	]
	for subject in subjects:
		subject_label = Label(window,text = subject, fg = "#00293c", font = "Arial 10", highlightbackground ="#acd0c0", height = 2, width = 22,borderwidth=2, relief="groove")
		subject_label.place(x = 135, y = id_pos_y,width = 200,height=30)
		id_pos_y += 30

	id_pos_y = 150
	exam_dates = ["dd/mm/yyyy",
	"dd/mm/yyyy",
	]

	for exam_date in exam_dates:
		subject_label = Label(window,text = exam_date, fg = "#00293c", font = "Arial 10",  highlightbackground ="#acd0c0", height = 2, width = 12,borderwidth=2, relief="groove")
		subject_label.place(x = 335, y = id_pos_y,width = 150,height=30)
		id_pos_y += 30

	go_back(window, return_function)
	sign_out(window)