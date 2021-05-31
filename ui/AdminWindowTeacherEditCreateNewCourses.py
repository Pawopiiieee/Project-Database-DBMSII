from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askquestion,showinfo
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
import ui.AdminWindowTeacherAddEditCourses
from functools import partial
from model.Teacher import *
from model.Person import *
from model.Course import *
from model.Study import *


def add_remove_courses(window, return_function,teacher,person):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Teacher Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 100, y = 15)

	teacherName_label = Label(window, text = "TeacherName", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacherName_label.place(x=20, y = 100)
	teacherName = Label(window, text = (str(person.lname) +"  "+ str(person.fname)), fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacherName.place(x=120, y = 100)

	teacher_id_label = Label(window, text = "Teacher ID", fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacher_id_label.place(x=20, y = 130)
	teacher_id = Label(window, text = teacher.teacherID, fg = "#006386", font="Arial 10 bold",bg = "#EBEBE9")
	teacher_id.place(x=120, y = 130)

	num_pos_y = 180
	num_pos_y2 = 210

	studies = Study.load_all()
	studynames = []
	for s in studies:
		studynames.append(s.studyname)

	courses_ini = []
	study_ini = []

	for i in range (5):

		selected_study = Label(window, text = "Select Study",fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9" )
		selected_study.place(x = 20, y = num_pos_y)
		selected_study = StringVar()
		
		study_ch = ttk.Combobox(window,textvariable = selected_study)
		study_ch["value"] = studynames
		study_ch["state"] = "readonly"
		study_ch.place(x = 150, y = num_pos_y)
		study_ini.append(study_ch)

		def study_changed (index, course_ch, event):
			# update the courses combobox
			selected_study_name = study_ini[index].get()
			study_idx = studynames.index(selected_study_name)
			study_courses = studies[study_idx].getCoursesInStudy()
			course_names = []
			for c in study_courses:
				course_names.append(c.coursetitle)

			course_ch["value"] = course_names

			confirm_msg = f"You Selected {selected_study_name}!"
			showinfo(title="Result", message= confirm_msg)

		num_pos_y += 70

		select_coures = Label(window, text = "Select Course",fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9" )
		select_coures.place(x = 20, y = num_pos_y2)
		selected_course = StringVar()
		
		courses_ch = ttk.Combobox(window,textvariable = selected_course)
		courses_ch["value"] = []
		courses_ch["state"] = "readonly"
		courses_ch.place(x = 150, y = num_pos_y2)
		courses_ini.append(courses_ch)

		study_ini[i].bind("<<ComboboxSelected>>", partial(study_changed,i, courses_ch))

		def course_changed (index,event):
			confirm_msg = f"You Selected {courses_ini[index].get()}!"
			showinfo(title="Result", message= confirm_msg)

		courses_ini[i].bind("<<ComboboxSelected>>", partial(course_changed,i))
		num_pos_y2 += 70

	def submit_all():
		result = askquestion(title="Confirmation", message= "Do you want to process?")
		#get_study = selected_study.get()
		#get_course = selected_course.get()
		if result == "yes":
			for i in range (5):
				selected_study_name = study_ini[i].get()
				selected_course_name = courses_ini[i].get()

				if selected_study_name != '' and selected_course_name != '':
					study_idx = studynames.index(selected_study_name)
					study_courses = studies[study_idx].getCoursesInStudy()
					for c in study_courses:
						if selected_course_name == c.coursetitle:
							c.teacherID = teacher.teacherID
							c.update()

			ui.AdminWindowTeacherAddEditCourses.teacher_edit_courses(window,return_function,teacher,person) #avoid circular import


	submit_text = Button(window, text = "Submit",font = "Arial 14 bold",fg = "#006386",highlightbackground ="#48C9B0",height =1, width = 6, command =submit_all,cursor = get_handcursor())
	submit_text.place(x=200, y = 550)


	go_back(window, return_function)
	sign_out(window)