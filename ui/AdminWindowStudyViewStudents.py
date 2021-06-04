from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askquestion
from ui.AdminWindowStudyViewStudentAdd import view_students_add
from functools import partial
from ui.Helpers import clear_window, go_back, get_handcursor
from ui.SignOut import sign_out

def view_students(window, return_function,study):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window,text = "Study: ", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)
	study_label = Label(window, text = study.studyname, fg = "#006386", font = "Arial 16 bold", bg ="#EBEBE9")
	study_label.place(x = 120, y = 100)

	add_student = Button(window,text = "Add + ",fg = "#006386", font = "Arial 10 bold", cursor = get_handcursor(),highlightbackground = "#006386",command = partial(view_students_add, window, return_function,study))
	add_student.place(x = 400, y = 100)

	student_name_label = Label(window, text = "Lastname   Firstname", fg = "#e6b800", font="Arial 10 bold",bg ="#006386")
	student_name_label.place(x=20, y = 140, width = 250,height = 30)
	student_id_label = Label(window, text = "Student ID", fg = "#e6b800", font="Arial 10 bold",height = 1, width = 13,bg ="#006386")
	student_id_label.place(x=270, y = 140, width = 100,height = 30)
	action_label = Label(window, text = "Action",fg = "#e6b800", font="Arial 10 bold",height = 1, width = 10,bg ="#006386")
	action_label.place(x=370, y = 140, width = 100,height = 30)

	num_pos_y =166
	y_position = 168

	students = study.getStudentsEnrolledInStudy()

	for i in range (len(students)):

		person = students[i].getPerson()

		lastName_label = Label(window, text = person.fname + " " + person.lname,fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		lastName_label.place(x = 20, y = num_pos_y, width = 250,height=30)

		studentID_label = Label(window, text = students[i].studentID,fg = "#00293c", font = "Arial 10",relief="ridge",borderwidth=2)
		studentID_label.place(x = 270 , y = num_pos_y,width =100,height=30)

		bg_label = Label(window, relief="ridge",borderwidth=2)
		bg_label.place(x=370, y= num_pos_y,width = 100,height=30)

		def confirm_deletion(student):
			result = askquestion(title="Confirmation", message= "Do you want to delete this data?")
			if result == "yes":
				student.enrolled = None
				student.update()
			view_students(window,return_function,study)
		delete_button = Button(window, text = "Delete",font = "Arial 10", fg = "#006386",highlightbackground = "#ffcccc",bg = "#ffcccc",cursor = get_handcursor(), height = 1,width = 5, relief = FLAT, command = partial(confirm_deletion, students[i]))
		delete_button.place(x= 400, y = y_position)

		num_pos_y += 30
		y_position += 30

	go_back(window, return_function)
	sign_out(window)
