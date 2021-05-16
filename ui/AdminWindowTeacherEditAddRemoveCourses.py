from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import askquestion,showinfo
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
import ui.AdminWindowTeacherEditCourses
from functools import partial


def add_remove_courses(window, return_function):
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

	num_pos_y = 180
	num_pos_y2 = 210
	courses_ini = []
	study_ini = []
	for i in range (5):

		selected_study = Label(window, text = "Select Study",fg = "#006386", font = "Alice 12 bold", bg ="#EBEBE9" )
		selected_study.place(x = 20, y = num_pos_y)
		selected_study = StringVar()
		studies = ["abc","def","ghi","jkl","mno"]
		study_ch = ttk.Combobox(window,textvariable = selected_study)
		study_ch["value"] = studies
		study_ch["state"] = "readonly"
		study_ch.place(x = 150, y = num_pos_y)
		study_ini.append(study_ch)
		def study_changed (coures_index,event):
			confirm_msg = f"You Selected {study_ini[coures_index].get()}!"
			showinfo(title="Result", message= confirm_msg)
		study_ini[i].bind("<<ComboboxSelected>>", partial(study_changed,i))
		num_pos_y += 70


		select_coures = Label(window, text = "Select Course",fg = "#006386", font = "Alice 12 bold", bg ="#EBEBE9" )
		select_coures.place(x = 20, y = num_pos_y2)
		selected_course = StringVar()
		courses = ["abc","def","ghi","jkl","mno"]
		courses_ch = ttk.Combobox(window,textvariable = selected_course)
		courses_ch["value"] = courses
		courses_ch["state"] = "readonly"
		courses_ch.place(x = 150, y = num_pos_y2)
		courses_ini.append(courses_ch)
		def course_changed (coures_index,event):
			confirm_msg = f"You Selected {courses_ini[coures_index].get()}!"
			showinfo(title="Result", message= confirm_msg)
		courses_ini[i].bind("<<ComboboxSelected>>", partial(course_changed,i))
		num_pos_y2 += 70

	def submit_all():
		result = askquestion(title="Confirmation", message= "Do you want to process?")
		get_study = selected_study.get()
		get_course = selected_course.get()

		print(get_study,get_course)
		if result == "yes":
			ui.AdminWindowTeacherEditCourses.teacher_edit_courses(window, return_function) #avoid circular import
		

	submit_text = Button(window, text = "Submit",font = "Alice 20 bold",fg = "#006386",highlightbackground ="#48C9B0",height = 2, width = 6, command =submit_all,cursor = "pointinghand")
	submit_text.place(x=200, y = 550)


	go_back(window, return_function)
	sign_out(window)