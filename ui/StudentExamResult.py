from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from ui.StudentExamStudyProgress import student_studyProgress
from functools import partial


def student_results(window, return_function): #this is going to show personal data
	clear_window(window)

	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Results", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 180, y = 15)

	code_label = Label(window,text = "Course ID", fg = "#00293c", font = "Arial 10", bg ="#e6f2ff", height = 2,width = 12,borderwidth=2, relief="groove")
	code_label.place(x = 35, y = 150, width= 100,height=30)
	subject_label = Label(window,text = "Subject", fg = "#00293c", font = "Arial 10", bg ="#e6f2ff", height = 2,width = 22,borderwidth=2, relief="groove")
	subject_label.place(x = 135, y = 150, width= 235,height=30)
	exam_label = Label(window,text = "Result", fg = "#00293c", font = "Arial 10", bg ="#e6f2ff", height = 2,width = 12,borderwidth=2, relief="groove")
	exam_label.place(x = 370, y = 150, width= 100,height=30)


	id_pos_y = 180
	courses_ids = [
		"abc123",
		"def456",
		"xy987"
	]

	for course_id in courses_ids:
		courseID_label = Label(window,text = course_id, fg = "#00293c", font = "Arial 10", bg ="#e6f2ff", height = 2, width = 12,borderwidth=2, relief="groove")
		courseID_label.place(x = 35, y = id_pos_y, width= 100,height=30)
		id_pos_y += 30


	subjects = ["acb",
	"edf",
	"ghi"
	]
	id_pos_y = 180
	for subject in subjects:
		subject_label = Label(window,text = subject, fg = "#00293c", font = "Arial 10", bg ="#e6f2ff", height = 2, width = 22,borderwidth=2, relief="groove")
		subject_label.place(x = 135, y = id_pos_y, width= 235,height=30)
		id_pos_y += 30

	id_pos_y = 180
	results = [10,
	9,
	5,
	]

	for result in results:
		if result < 6:
			subject_label = Label(window,text = result, fg = "red", font = "Arial 10", bg ="#e6f2ff", height = 2, width = 12,borderwidth=2, relief="groove")
			subject_label.place(x = 370, y = id_pos_y, width= 100,height=30)
			id_pos_y += 30
		else:
			subject_label = Label(window,text = result, fg = "#2eb82e", font = "Arial 10", bg ="#e6f2ff", height = 2, width = 12,borderwidth=2, relief="groove")
			subject_label.place(x = 370, y = id_pos_y, width= 100,height=30)
			id_pos_y += 30

	exam_label = Button(window,text = "Study Progress", fg = "#2E4053", font = "Arial 12 bold", highlightbackground ="#48C9B0", height = 1,width = 15,borderwidth=2, relief="groove",cursor = get_handcursor(),command = partial(student_studyProgress,window,return_function))
	exam_label.place(x = 170, y = 550)




	go_back(window, return_function)
	sign_out(window)