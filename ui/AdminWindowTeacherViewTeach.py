from tkinter import *
from tkinter import ttk
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from model.Teacher import *
from model.Person import *
from model.Course import *
from model.Study import *

def teaching_courses(window, return_function,teacher,person):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Teacher Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 100, y = 15)

	teacherName_label = Label(window, text = "TeacherName", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacherName_label.place(x=20, y = 100)
	teacherName = Label(window, text = (str(person.fname) + " " + str(person.lname)), fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacherName.place(x=120, y = 100)

	teacher_id_label = Label(window, text = "Teacher ID", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacher_id_label.place(x=20, y = 130)
	teacher_id = Label(window, text = teacher.teacherID, fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacher_id.place(x=120, y = 130)

	courses_label = Label(window, text = "Course Name",fg = "#e6b800", font="Arial 10 bold", bg ="#006386")
	courses_label.place(x=20, y = 170,width = 180, height=30)

	courseID_label = Label(window, text = "Course ID",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	courseID_label.place(x=200, y = 170,width = 100,height=30)

	study_label = Label(window, text = "Study",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	study_label.place(x=300,  y = 170,width = 180,height=30)

	courses = teacher.getTeacherCourses()

	num_pos_y = 200

	for i in range (len(courses)):

		course_lab = Label(window, text =courses[i].coursetitle,fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		course_lab.place(x = 20, y = num_pos_y,width = 180,height=30)

		courseID_lab = Label(window, text = courses[i].courseID,fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		courseID_lab.place(x = 200 , y = num_pos_y,width = 100,height=30)

		study = courses[i].getStudy()
		study_lab = Label(window, text = study.studyname,fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		study_lab.place(x = 300 , y = num_pos_y,width = 180,height=30)

		num_pos_y += 30


	go_back(window, return_function)
	sign_out(window)
