from tkinter import *
from tkinter import ttk
import ui.TeacherCourses
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from functools import partial
from model.Course import *
from model.Study import *

def courseView_students(window, return_function,teacher,person,course):#this is going to show the course the teacher is currently teaching
	clear_window(window)

	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Courses", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 180, y = 15)

	teacherName_label = Label(window, text = "Name", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacherName_label.place(x=20, y = 100)
	name_label = Label(window, text = (str(person.lname) + "  " + str(person.fname)),fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	name_label.place(x = 120, y = 100)

	teacher_id_label = Label(window, text = "Teacher ID", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacher_id_label.place(x=20, y = 130)
	teacherID = Label(window, text = teacher.teacherID,fg = "#00293c", font = "Arial 10", bg ="#EBEBE9")
	teacherID.place(x= 120, y = 130)

	courseName_label = Label(window, text = "Course Name",fg = "#006386", font="Arial 10 bold",bg ="#EBEBE9")
	courseName_label.place(x=20, y = 160)
	cName_label = Label(window, text = course.coursetitle,fg = "#006386", font="Arial 10 bold",bg ="#EBEBE9")
	cName_label.place(x=120, y = 160)

	courseID_label = Label(window, text = "Course ID",fg = "#006386", font="Arial 10 bold",bg ="#EBEBE9")
	courseID_label.place(x=20, y = 190)
	cID_label = Label(window, text = course.courseID,fg = "#006386", font="Arial 10 bold",bg ="#EBEBE9")
	cID_label.place(x=120, y = 190)

	credit_label = Label(window,text = "Credits", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	credit_label.place(x = 270, y = 190)
	cre_label = Label(window,text = course.credits, fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	cre_label.place(x = 370, y = 190)

	student_name_label = Label(window, text = "Student Name", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	student_name_label.place(x=20, y = 220,width = 250,height=30)
	student_id_label = Label(window, text = "Student ID", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	student_id_label.place(x=270, y = 220,width = 100,height=30)
	grade_label = Label(window, text = "Grade",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	grade_label.place(x=370, y = 220,width = 85,height=30)

	studentIncourse = course.getStudentsInCourse()
	all_exams = course.getExams()
	exam = all_exams[0]
	num_pos_y = 250

	grade_point = []
	for i in range (len(studentIncourse)):
		person = studentIncourse[i].getPerson()

		lastName_label = Label(window, text =  str(person.lname) + "  "+ str(person.fname),fg = "#00293c", font = "Arial 13",relief="ridge",borderwidth=2)
		lastName_label.place(x = 20, y = num_pos_y,width = 250,height=30)

		studentID_label = Label(window, text = studentIncourse[i].studentID,fg = "#00293c", font = "Arial 13",relief="ridge",borderwidth=2)
		studentID_label.place(x = 270 , y = num_pos_y,width = 100,height=30)

		input_grade = Text(window, height = 2, width = 10, bg = "#80DEEA",highlightbackground ="#EBEBE9", font = "Arial 10 bold",relief=FLAT)
		input_grade.place(x=370, y = num_pos_y, width = 100,height = 30)

		oldResult = exam.getStudentGrade(studentIncourse[i].studentID)
		if oldResult != None:
			input_grade.insert(END, oldResult.grade)
		num_pos_y += 30
		grade_point.append(input_grade)
	return_course = Button(window,text = "Return", fg = "#2E4053", font = "Arial 15 bold",bg = "#48C9B0", highlightbackground ="#48C9B0", height = 1,width = 10,borderwidth=2,cursor = get_handcursor(), relief="groove", command = partial(ui.TeacherCourses.course,window, return_function))
	return_course.place(x = 170, y = 500)

	go_back(window, return_function)
	sign_out(window)
