from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askquestion,showerror
import ui.AdminWindowStudyViewCourses
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from functools import partial
from model import Course
from model.Result  import Result


def submit_grade_courses(window, return_function,course):
#controll part
	def confirm_submit():
		has_incorrect_grade = False
		for g in range(len(grade_point)):
			text_button = grade_point[g]
			grade = text_button.get(1.0, "end-1c")
		
			if int(grade) < 0 or int(grade) > 100:
				has_incorrect_grade = True

		if has_incorrect_grade:
			showerror(title="Error", message= "Invalid Grade Point!",icon ="error")
		else:
			result = askquestion(title="Confirmation", message= "Do you want to confirm?")
			if result == "yes":
				exam_id = exam.examID
				for g in range(len(grade_point)):
					student_id = studentIncourse[g].studentID
					currentResult = exam.getStudentGrade(student_id)
					grade = int(grade_point[g].get(1.0, "end-1c"))
					if currentResult == None: #no dubplicate grades for the same student / course. >> check db before adding it
						result = Result()
						result.grade = grade
						result.examID = exam_id
						result.studentID = student_id
						result.insert()
					else:
						currentResult.grade = grade
						currentResult.update()

				ui.AdminWindowStudyViewCourses.view_courses(window, return_function,course.getStudy())

#view part
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window,text = "Course Title ", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)

	title = Label(window,text = course.coursetitle, fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	title.place(x = 120, y = 100)

	credit_label = Label(window,text = "Credits", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	credit_label.place(x = 20, y = 130)

	credit = Label(window,text =course.credits, fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	credit.place(x = 120, y = 130)

	student_name_label = Label(window, text = "Student Name", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	student_name_label.place(x=20, y = 180, width = 250,height = 30)
	student_id_label = Label(window, text = "Student ID", fg = "#e6b800", font="Arial 10 bold",height = 1, width = 13,bg ="#006386")
	student_id_label.place(x=270, y = 180, width = 100,height = 30)
	grade_label = Label(window, text = "Grade",fg = "#e6b800", font="Arial 10 bold",height = 1, width = 10,bg ="#006386")
	grade_label.place(x=370, y = 180, width = 100,height = 30)

	all_exams = course.getExams()
	exam = all_exams[0]
	studentIncourse = course.getStudentsInCourse()
	num_pos_y = 210

	grade_point = []
	for i in range (len(studentIncourse)):
		person = studentIncourse[i].getPerson()

		studentName_label = Label(window, text = str(person.lname) + "  "+ str(person.fname),fg = "#00293c", font = "Arial 10", relief="ridge",borderwidth=2)
		studentName_label.place(x = 20, y = num_pos_y, width = 250,height = 30)

		studentID_label = Label(window, text = studentIncourse[i].studentID,fg = "#00293c", font = "Arial 10",  relief="ridge",borderwidth=2)
		studentID_label.place(x = 270 , y = num_pos_y, width = 100,height = 30)

		input_grade = Text(window, height = 2, width = 10, bg = "#80DEEA",highlightbackground ="#EBEBE9", font = "Arial 10 bold",relief=FLAT)
		input_grade.place(x=370, y = num_pos_y, width = 100,height = 30)

		oldResult = exam.getStudentGrade(studentIncourse[i].studentID)
		if oldResult != None:
			input_grade.insert(END, oldResult.grade)
		num_pos_y += 30
		grade_point.append(input_grade)
	submit_text = Button(window, text = "Submit",font = "Arial 14 bold",fg = "#006386",highlightbackground ="#48C9B0", command = confirm_submit,cursor = get_handcursor())
	submit_text.place(x=200, y = 550, width = 120,height = 30)

	go_back(window, return_function)
	sign_out(window)
