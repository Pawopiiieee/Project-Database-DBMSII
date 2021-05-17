from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import askquestion,showerror
import ui.AdminWindowStudyViewCourses
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial


def submit_grade_courses(window, return_function):
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
				ui.AdminWindowStudyViewCourses.view_courses(window, return_function)
#view part
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window,text = "Course Title ", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)

	credit_label = Label(window,text = "Credits", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	credit_label.place(x = 20, y = 130)

	student_name_label = Label(window, text = "Student Name", fg = "#e6b800", font="Alice 13 bold",height = 1, width = 25,bg ="#006386")
	student_name_label.place(x=20, y = 180)
	student_id_label = Label(window, text = "Student ID", fg = "#e6b800", font="Alice 13 bold",height = 1, width = 13,bg ="#006386")
	student_id_label.place(x=250, y = 180)	
	grade_label = Label(window, text = "Grade",fg = "#e6b800", font="Alice 13 bold",height = 1, width = 10,bg ="#006386")
	grade_label.place(x=370, y = 180)

	lastname_students = ["abc","def","ghi","jkl","mno"]
	firstname_students = ["mnb","kgb","cni","kpn","zos"]
	id_student= ["12345","22345","32345","42345","52345"]
	num_pos_y = 202

	grade_point = []
	for i in range (len(lastname_students)):
		lastName_label = Label(window, text = lastname_students[i] + "   "  + firstname_students[i],fg = "#00293c", font = "Alice 13", height = 2, width = 25,relief="ridge",borderwidth=2)
		lastName_label.place(x = 20, y = num_pos_y)

		studentID_label = Label(window, text = id_student[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 13,relief="ridge",borderwidth=2)
		studentID_label.place(x = 250 , y = num_pos_y)
		
		input_grade = Text(window, height = 2, width = 10, bg = "#80DEEA",highlightbackground ="#EBEBE9", font = "Alice 13 bold",relief=FLAT)
		input_grade.place(x=370, y = num_pos_y)
		num_pos_y += 30
		grade_point.append(input_grade)
	submit_text = Button(window, text = "Submit",font = "Alice 20 bold",fg = "#006386",highlightbackground ="#48C9B0",height = 2, width = 6, command = confirm_submit,cursor = "pointinghand")
	submit_text.place(x=200, y = 550)

	go_back(window, return_function)
	sign_out(window)
