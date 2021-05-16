from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import askquestion
from ui.AdminWindowTeacherEditAddRemoveCourses import add_remove_courses
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial
import ui.AdminWindowTeacherViewTeach
def teacher_edit_courses(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Teacher Overview", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 120, y = 15)

	teacherName_label = Label(window, text = "TeacherName", fg = "#006386", font="Alice 13 bold",bg = "#EBEBE9")
	teacherName_label.place(x=20, y = 100)
	teacher_id_label = Label(window, text = "Teacher ID", fg = "#006386", font="Alice 13 bold",bg = "#EBEBE9")
	teacher_id_label.place(x=20, y = 130)

	create_data_text = Button(text = "Create new data", fg = "#e6b800", font="Alice 14 bold",height = 2, width = 15, cursor = "pointinghand", highlightbackground =  "#006386", command = partial (add_remove_courses,window,return_function))
	create_data_text.place(x=330, y = 170)
	

	Courses_label = Label(window, text = "Course Name",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 18,bg ="#006386")
	Courses_label.place(x=15, y = 220)

	CourseID_label = Label(window, text = "Course ID",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 8,bg ="#006386")
	CourseID_label.place(x=180, y = 220)

	study_label = Label(window, text = "Study",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 19,bg ="#006386")
	study_label.place(x=250, y = 220)

	action_label = Label(window, text = "Action",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 6,bg ="#006386")
	action_label.place(x=427, y = 220)


	courses = ["abc","def","ghi","jkl","mno"]
	course_id= ["AA12345","AA22345","AA32345","AA42345","AA52345"]
	studies = ["xxx","yyy","zzz","jkl","mno"]
	num_pos_y = 257
	y_position = 263
	for i in range (len(courses)):

		course_lab = Label(window, text = courses[i],fg = "#00293c", font = "Alice 13", height = 2, width = 18,relief="ridge",borderwidth=2)
		course_lab.place(x = 15, y = num_pos_y)

		courseID_label = Label(window, text = course_id[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 8,relief="ridge",borderwidth=2)
		courseID_label.place(x = 180 , y = num_pos_y)

		study_lab = Label(window, text = studies[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 19,relief="ridge",borderwidth=2)
		study_lab.place(x = 250 , y = num_pos_y)

		bg_label = Label(window, height = 2,width = 6,relief="ridge",borderwidth=2)
		bg_label.place(x=427, y= num_pos_y)

		def confirm_deletion():
			askquestion(title="Delete Data", message= "Do you want to process?",icon = "warning")

		delete_button = Button(window, text = "Delete",font = "Alice 13", fg = "#006386",highlightbackground = "#ffcccc",cursor = "pointinghand", height = 1,width = 6, relief = FLAT, command = confirm_deletion)
		delete_button.place(x= 427, y = y_position)
		y_position += 30
		num_pos_y += 30
	def submit_edit():
		result = askquestion(title="Confirmation", message= "Do you want to process?")
		if result == "yes":
			ui.AdminWindowTeacherViewTeach.teaching_courses(window, return_function) #avoid circular import

	submit_text = Button(window, text = "Submit",font = "Alice 20 bold",fg = "#006386",highlightbackground ="#48C9B0",height = 2, width = 6, command =submit_edit,cursor = "pointinghand")
	submit_text.place(x=200, y = 530)

	go_back(window, return_function)
	sign_out(window)
