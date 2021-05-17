from tkinter import *
from tkinter import messagebox 
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial
from tkinter import ttk 
from tkinter.messagebox import showinfo
from ui.TeacherCoursesStudy import courseView_students


def course(window, return_function):#this is going to show the course the teacher is currently teaching
	clear_window(window)

	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Courses", fg = "#EBEBE9", font = "Alice 35", bg ="#006386")
	header_label.place(x = 180, y = 15)
	
	teacherName_label = Label(window, text = "TeacherName", fg = "#006386", font="Alice 13 bold",bg = "#EBEBE9")
	teacherName_label.place(x=20, y = 100)
	teacher_id_label = Label(window, text = "Teacher ID", fg = "#006386", font="Alice 13 bold",bg = "#EBEBE9")
	teacher_id_label.place(x=20, y = 130)
	
	courses_label = Label(window, text = "Course Name",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 18,bg ="#006386")
	courses_label.place(x=45, y = 200)

	courseID_label = Label(window, text = "Course ID",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 8,bg ="#006386")
	courseID_label.place(x=200, y = 200)

	study_label = Label(window, text = "Study",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 19,bg ="#006386")
	study_label.place(x=270, y = 200)

	courses = ["abc","def","ghi","jkl","mno"]
	course_id= ["AA12345","AA22345","AA32345","AA42345","AA52345"]

	selected_study = StringVar()
	studies = ["abc","def","ghi","jkl","mno"]
	study_ch = ttk.Combobox(window,textvariable = selected_study,width = 20)
	study_ch["value"] = studies
	study_ch["state"] = "readonly"
	def study_changed (event):
		confirm_msg = f"You Selected {study_ch.get()}!"
		showinfo(title="Result", message= confirm_msg)
	study_ch.bind("<<ComboboxSelected>>", study_changed)
	study_ch.place(x = 80, y = 160)
	study_label = Label(window,text = "Study", fg = "#006386", font = "Alice 14 bold", bg ="#EBEBE9")
	study_label.place(x = 20, y = 160)
	num_pos_y = 237
	
	for i in range (len(courses)):

		course_lab = Button(window, text = courses[i],fg = "#00293c", font = "Alice 13", height = 2, width = 18,borderwidth=2,cursor = "pointinghand",command =partial(courseView_students,window,return_function))
		course_lab.place(x = 45, y = num_pos_y)

		courseID_lab = Label(window, text = course_id[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 8,relief="ridge",borderwidth=2)
		courseID_lab.place(x = 200 , y = num_pos_y)

		study_lab = Label(window, text = studies[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 19,relief="ridge",borderwidth=2)
		study_lab.place(x = 270 , y = num_pos_y)

		num_pos_y += 30

	

	go_back(window, return_function)
	sign_out(window)