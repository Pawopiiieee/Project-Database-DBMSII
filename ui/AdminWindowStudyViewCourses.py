from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askquestion
from ui.AdminWindowStudyViewCourseAdd import view_course_add
from ui.AdminWindowStudyViewCourseGrade import submit_grade_courses
from functools import partial
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from model import Study,Course

def view_courses(window, return_function,study):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window, text = "Study: ", fg = "#006386", font = "Arial 16 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)
	study_label = Label(window, text = study.studyname, fg = "#006386", font = "Arial 16 bold", bg ="#EBEBE9")
	study_label.place(x = 120, y = 100)

	add_course = Button(window,text = "Add + ",fg = "#006386", font = "Arial 12 bold", cursor = get_handcursor(),highlightbackground = "#006386",command = partial(view_course_add, window, return_function,study))
	add_course.place(x = 400, y = 100)

	course_name_label = Label(window, text = "Courses", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	course_name_label.place(x=20, y = 140, width=250, height= 30)
	course_id_label = Label(window, text = "Course ID", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	course_id_label.place(x=270, y = 140, width=100, height= 30)
	action_label = Label(window, text = "Action",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	action_label.place(x=370, y = 140, width=100, height= 30)

	courses = study.getCoursesInStudy()
	num_pos_y = 167
	y_position = 172

	for i in range (len(courses)):

		courseName_label = Button(window, text = courses[i].coursetitle,fg = "#00293c", font = "Arial 10", height = 2, width = 25,relief="ridge",borderwidth=2,cursor = get_handcursor(), command = partial(submit_grade_courses, window, return_function,courses[i]))
		courseName_label.place(x = 20, y = num_pos_y, width=250, height= 30)

		courseID_label = Label(window, text = courses[i].courseID,fg = "#00293c", font = "Arial 10",  height = 2, width = 13,relief="ridge",borderwidth=2)
		courseID_label.place(x = 270 , y = num_pos_y, width=100, height= 30)

		bg_label = Label(window, relief="ridge",borderwidth=2)
		bg_label.place(x=370, y= num_pos_y, width=100, height= 30)

		def confirm_deletion():
			askquestion(title="Confirmation", message= "Do you want to delete this data?")
		delete_button = Button(window, text = "Delete",font = "Arial 10", fg = "#006386",bg = "#ffcccc",highlightbackground = "#ffcccc",cursor = get_handcursor(), height = 1,width = 5, relief = FLAT, command = confirm_deletion)
		delete_button.place(x= 390, y = y_position, width=70, height= 20)

		num_pos_y += 30
		y_position += 30

	go_back(window, return_function)
	sign_out(window)
