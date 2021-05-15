from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out

def study_overview_edit(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Modify Courses", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 130, y = 15)

	select_coures = Label(window, text = "Select a Course",fg = "#006386", font = "Alice 15", bg ="#EBEBE9" )
	select_coures.place(x = 20, y = 90)
	selected_course = StringVar()
	courses = ["abc","def","ghi","jkl","mno"]
	courses_sh = ttk.Combobox(window,textvariable = selected_course)
	courses_sh["value"] = courses
	courses_sh["state"] = "readonly"
	courses_sh.place(x = 170, y = 90)
	def course_changed (event):
		confirm_msg = f"You Selected {courses_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	courses_sh.bind("<<ComboboxSelected>>", course_changed)

	select_instructor = Label(window, text = "Select an Instructor",fg = "#006386", font = "Alice 15", bg ="#EBEBE9" )
	select_instructor.place(x = 20, y = 120)
	selected_instructor = StringVar()
	teachers = ["bob1","bob2","bob3","bob4","bob5"]
	instructor_sh = ttk.Combobox(window,textvariable = selected_instructor)
	instructor_sh["value"] = teachers
	instructor_sh["state"] = "readonly"
	instructor_sh.place(x = 170, y = 120)
	def instructor_changed (event):
		confirm_msg = f"You Selected {instructor_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	instructor_sh.bind("<<ComboboxSelected>>", instructor_changed)

	select_classroom = Label(window, text = "Select a Classroom",fg = "#006386", font = "Alice 15", bg ="#EBEBE9" )
	select_classroom.place(x = 20, y = 150)
	selected_classroom = StringVar()
	classrooms = ["A111","A112","A113","A114","A115"]
	classroom_sh = ttk.Combobox(window,textvariable = selected_classroom)
	classroom_sh["value"] = classrooms
	classroom_sh["state"] = "readonly"
	classroom_sh.place(x = 170, y = 150)
	def classroom_changed (event):
		confirm_msg = f"You Selected {instructor_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	instructor_sh.bind("<<ComboboxSelected>>", classroom_changed)

	show_desc = Label(window, text = "Description",fg = "#006386", font = "Alice 15", bg ="#EBEBE9" )
	show_desc.place(x = 20, y = 180)
	def get_desc():
		input_tex = input_text.get(1.0, "end-1c")
		print(input_tex)
	input_text = Text(window, height = 5, width = 45, bg = "light yellow", highlightbackground = "#006386", font = "Alice 12")
	input_text.place(x=115, y = 180)
	submit_text = Button(window, text = "Submit",font = "Alice 12 bold",fg = "#006386",highlightbackground ="#48C9B0",height = 1, width = 6, command =get_desc)
	submit_text.place(x=270, y = 270)

	select_semester = Label(window, text = "Select Semester",fg = "#006386", font = "Alice 15", bg ="#EBEBE9" )
	select_semester.place(x = 20, y = 295)

	selected_semester = IntVar()
	semesters = [1,2,3,4]
	semesters_sh = ttk.Combobox(window,textvariable = selected_semester)
	semesters_sh["value"] = semesters
	semesters_sh["state"] = "readonly"
	semesters_sh.place(x = 170, y = 295)
	def semester_changed (event):
		confirm_msg = f"You Selected {semesters_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	semesters_sh.bind("<<ComboboxSelected>>", semester_changed)

	subjects_label = Label(window, text = "Subjects", fg = "#e6b800", font="Alice 13 bold",height = 1, width = 30,bg ="#006386")
	subjects_label.place(x=20, y = 330)
	action_label = Label(window, text = "Actions",fg = "#e6b800", font="Alice 13 bold",height = 1, width = 28,bg ="#006386")
	action_label.place(x=290, y = 330)






	go_back(window, return_function)
	sign_out(window)



	

