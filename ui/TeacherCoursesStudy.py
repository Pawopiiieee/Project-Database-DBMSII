from tkinter import *
from tkinter import ttk
import ui.TeacherCourses
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from functools import partial

def courseView_students(window, return_function):#this is going to show the course the teacher is currently teaching
	clear_window(window)

	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Courses", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 180, y = 15)

	teacherName_label = Label(window, text = "TeacherName", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacherName_label.place(x=20, y = 100)
	teacher_id_label = Label(window, text = "Teacher ID", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacher_id_label.place(x=20, y = 130)

	courseName_label = Label(window, text = "Course Name",fg = "#006386", font="Arial 10 bold",bg ="#EBEBE9")
	courseName_label.place(x=20, y = 160)

	courseID_label = Label(window, text = "Course ID",fg = "#006386", font="Arial 10 bold",bg ="#EBEBE9")
	courseID_label.place(x=20, y = 190)

	credit_label = Label(window,text = "Credits", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	credit_label.place(x = 270, y = 190)

	student_name_label = Label(window, text = "Student Name", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	student_name_label.place(x=20, y = 250,width = 185,height=30)
	student_id_label = Label(window, text = "Student ID", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	student_id_label.place(x=250, y = 250,width = 185,height=30)
	grade_label = Label(window, text = "Grade",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	grade_label.place(x=370, y = 250,width = 185,height=30)

	lastname_students = ["abc","def","ghi","jkl","mno"]
	firstname_students = ["mnb","kgb","cni","kpn","zos"]
	id_student= ["12345","22345","32345","42345","52345"]
	num_pos_y = 270

	grade_point = []
	for i in range (len(lastname_students)):
		lastName_label = Label(window, text = lastname_students[i] + "   "  + firstname_students[i],fg = "#00293c", font = "Arial 13", height = 2, width = 25,relief="ridge",borderwidth=2)
		lastName_label.place(x = 20, y = num_pos_y)

		studentID_label = Label(window, text = id_student[i],fg = "#00293c", font = "Arial 13",  height = 2, width = 13,relief="ridge",borderwidth=2)
		studentID_label.place(x = 250 , y = num_pos_y)

		student_grade = Label(window, height = 2, width = 10, bg = "#F9E79F", font = "Arial 10 bold",relief="ridge",borderwidth=2)
		student_grade.place(x=370, y = num_pos_y)
		num_pos_y += 30
		grade_point.append(student_grade)

	return_course = Button(window,text = "Return", fg = "#2E4053", font = "Arial 15 bold",bg = "#48C9B0", highlightbackground ="#48C9B0", height = 1,width = 10,borderwidth=2,cursor = get_handcursor(), relief="groove", command = partial(ui.TeacherCourses.course,window, return_function))
	return_course.place(x = 170, y = 500)

	go_back(window, return_function)
	sign_out(window)
