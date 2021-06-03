from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from ui.StudentExamStudyProgress import student_studyProgress
from functools import partial
from model import Student,Study,Person


def student_results(window, return_function,student,person): #this is going to show personal grade points
	clear_window(window)

	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Results", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 180, y = 15)

	code_label = Label(window,text = "Course ID", fg = "#00293c", font = "Arial 11 bold", bg ="#e6f2ff", height = 2,width = 12,borderwidth=2, relief="groove")
	code_label.place(x = 35, y = 120, width= 100,height=30)
	subject_label = Label(window,text = "Subject", fg = "#00293c", font = "Arial 11 bold", bg ="#e6f2ff", height = 2,width = 22,borderwidth=2, relief="groove")
	subject_label.place(x = 135, y = 120, width= 235,height=30)
	exam_label = Label(window,text = "Result", fg = "#00293c", font = "Arial 11 bold", bg ="#e6f2ff", height = 2,width = 12,borderwidth=2, relief="groove")
	exam_label.place(x = 370, y = 120, width= 100,height=30)

	id_pos_y = 150
	courses = student.getEnrolledCourses()
	for i in range (len(courses)):
		courseID_label = Label(window,text = courses[i].courseID, fg = "#00293c", font = "Arial 10", bg ="#e6f2ff", height = 2, width = 12,borderwidth=2, relief="groove")
		courseID_label.place(x = 35, y = id_pos_y, width= 100,height=30)
		subject_label = Label(window,text = courses[i].coursetitle, fg = "#00293c", font = "Arial 10", bg ="#e6f2ff", height = 2, width = 22,borderwidth=2, relief="groove")
		subject_label.place(x = 135, y = id_pos_y, width= 235,height=30)
		grade_label = Label(window, bg ="#e6f2ff",borderwidth=2, relief="groove")
		grade_label.place(x = 370, y = id_pos_y, width= 100,height=30)
		id_pos_y += 30

	grades = student.getStudentGrades()
	id_pos = 150
	for i in range (len(grades)):
		student_grade = grades[i].grade
		if student_grade >= 55:
			grade_label = Label(window,text = student_grade, fg = "green", font = "Arial 10", bg ="#e6f2ff",borderwidth=2, relief="groove")
			grade_label.place(x = 370, y = id_pos, width= 100,height=30)
			
		else:	
			grade_label = Label(window,text = student_grade, fg = "red", font = "Arial 10", bg ="#e6f2ff",borderwidth=2, relief="groove")
			grade_label.place(x = 370, y = id_pos, width= 100,height=30)
	
		id_pos += 30

	exam_label = Button(window,text = "Study Progress", fg = "#2E4053", font = "Arial 12 bold", highlightbackground ="#48C9B0", height = 1,width = 15,borderwidth=2, relief="groove",cursor = get_handcursor(),command = partial(student_studyProgress,window,return_function,student,person))
	exam_label.place(x = 170, y = 550)




	go_back(window, return_function)
	sign_out(window)