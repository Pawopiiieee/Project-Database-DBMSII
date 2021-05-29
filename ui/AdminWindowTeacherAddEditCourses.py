from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askquestion
from ui.AdminWindowTeacherEditCreateNewCourses import add_remove_courses
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from functools import partial
import ui.AdminWindowTeacherViewTeach
def teacher_edit_courses(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Teacher Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 120, y = 15)

	teacherName_label = Label(window, text = "TeacherName", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacherName_label.place(x=20, y = 100)
	teacher_id_label = Label(window, text = "Teacher ID", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacher_id_label.place(x=20, y = 130)

	create_data_text = Button(text = "Create new data", fg = "#e6b800", font="Arial 10 bold", width = 15, cursor = get_handcursor(), highlightbackground =  "#006386", command = partial (add_remove_courses,window,return_function))
	create_data_text.place(x=330, y = 170,height=40)


	Courses_label = Label(window, text = "Course Name",fg = "#e6b800", font="Arial 10 bold", width = 20,bg ="#006386")
	Courses_label.place(x=15, y = 220, height=30)

	CourseID_label = Label(window, text = "Course ID",fg = "#e6b800", font="Arial 10 bold", width = 12,bg ="#006386")
	CourseID_label.place(x=175, y = 220, height=30)

	study_label = Label(window, text = "Study",fg = "#e6b800", font="Arial 10 bold", width = 20,bg ="#006386")
	study_label.place(x=265, y = 220, height=30)

	action_label = Label(window, text = "Action",fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	action_label.place(x=427, y = 220, width=55,height=30)


	courses = ["abc","def","ghi","jkl","mno"]
	course_id= ["AA12345","AA22345","AA32345","AA42345","AA52345"]
	studies = ["xxx","yyy","zzz","jkl","mno"]
	num_pos_y = 250
	y_position = 253
	for i in range (len(courses)):

		course_lab = Label(window, text = courses[i],fg = "#00293c", font = "Arial 10", width = 20,relief="ridge",borderwidth=2)
		course_lab.place(x = 15, y = num_pos_y, height=30)

		courseID_label = Label(window, text = course_id[i],fg = "#00293c", font = "Arial 9", width = 12,relief="ridge",borderwidth=2)
		courseID_label.place(x = 180 , y = num_pos_y, height=30)

		study_lab = Label(window, text = studies[i],fg = "#00293c", font = "Arial 10", width =20,relief="ridge",borderwidth=2)
		study_lab.place(x = 265 , y = num_pos_y, height=30)

		bg_label = Label(window,relief="ridge",borderwidth=2)
		bg_label.place(x=427, y= num_pos_y,width = 55, height=30)

		def confirm_deletion():
			askquestion(title="Delete Data", message= "Do you want to process?",icon = "warning")

		delete_button = Button(window, text = "Delete",font = "Arial 8", fg = "#006386",bg =  "#ffcccc", highlightbackground = "#ffcccc",cursor = get_handcursor(),width = 4, relief = FLAT, command = confirm_deletion)
		delete_button.place(x= 435, y = y_position, height=26)
		y_position += 30
		num_pos_y += 30
	def submit_edit():
		result = askquestion(title="Confirmation", message= "Do you want to process?")
		if result == "yes":
			ui.AdminWindowTeacherViewTeach.teaching_courses(window, return_function) #avoid circular import

	submit_text = Button(window, text = "Submit",font = "Arial 14 bold",fg = "#006386",highlightbackground ="#48C9B0",height = 1, width = 6, command =submit_edit,cursor = get_handcursor())
	submit_text.place(x=200, y = 530)

	go_back(window, return_function)
	sign_out(window)
