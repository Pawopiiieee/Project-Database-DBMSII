from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.AdminWindowStudentView import student_view
from ui.AdminWindowStudentEdit import student_edit
from ui.AdminWindowStudentCreateNew import createNew_student
from tkinter.messagebox import askquestion
from ui.Helpers import clear_window, go_back, get_handcursor
from ui.SignOut import sign_out
from functools import partial

from model.Student import *

def admin_window_students(window,return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "An Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 150, y = 15)

	create_data_text = Button(text = "+ Create new data", fg = "#e6b800", font="Arial 12 bold", bg = "#2F4F4F", width = 15, cursor = get_handcursor(), highlightbackground =  "#006386", command = partial(createNew_student,window,return_function))
	create_data_text.place(x=10, y = 80, height = 40)

	header_label1 = Label(window, text = "#",fg = "#e6b800", font="Arial 13 bold",bg ="#006386")
	header_label1.place(x=10, y = 125, width=30, height=30)
	header_label2 = Label(window, text = "Lastname",fg = "#e6b800", font="Arial 13 bold", bg ="#006386")
	header_label2.place(x=40,y = 125,width=150, height=30)
	header_label3 = Label(window, text = "Firstname",fg = "#e6b800", font="Arial 13 bold", width = 15,bg ="#006386" )
	header_label3.place(x=180, y = 125, width=150,height=30)
	header_label4 = Label(window, text = "Action",fg = "#e6b800", font="Arial 13 bold" ,bg ="#006386" )
	header_label4.place(x=320, y = 125, width=165, height=30)

	students = Student.load_all()
	num_pos_y = 158
	#initial_num = 0
	y_position = 160
	for i in range (len(students)):
		person = students[i].getPerson()
		number_label = Label(window, text = (i + 1),fg = "#00293c", font = "Arial 13")
		number_label.place(x = 10, y = num_pos_y,width=30, height=30)
		#initial_num += 1
		last_name_label = Label(window, text = person.lname,fg = "#00293c", font = "Arial 13")
		last_name_label.place(x = 40, y = num_pos_y,width=150, height=30)

		first_name_label = Label(window, text = person.fname,fg = "#00293c", font = "Arial 13")
		first_name_label.place(x = 180 , y = num_pos_y,width=150, height=30)
		bg_label = Label(window)
		bg_label.place(x=320, y= num_pos_y, width = 165, height=30)
		num_pos_y += 30

		view_button = Button(window, text = "View",font = "Arial 10", fg = "#006386",bg = "#ccd9ff",highlightbackground = "#ccd9ff",cursor = get_handcursor(), height = 1,width = 4, relief = FLAT,command = partial(student_view, window, return_function, students[i], person))
		view_button.place(x= 330, y = y_position, height=26)
		edit_button = Button(window, text = "Edit",font = "Arial 10", fg = "#006386",bg = "#fff2cc",highlightbackground = "#fff2cc",cursor = get_handcursor(), height = 1,width = 4, relief = FLAT, command = partial(student_edit, window, return_function,students[i], person))
		edit_button.place(x= 380, y = y_position, height=26)

		def confirm_deletion(student):
			result = askquestion(title="Delete Data", message= "Do you want to process?",icon = "warning")
			if result == "yes":
				person = student.getPerson()
				student.delete()
				person.delete()
				admin_window_students(window,return_function)
		delete_button = Button(window, text = "Delete",font = "Arial 10", fg = "#006386",bg = "#ffcccc",highlightbackground = "#ffcccc",cursor = get_handcursor(), height = 1,width = 5, relief = FLAT, command = partial(confirm_deletion, students[i]))
		delete_button.place(x= 430, y = y_position, height=26)
		y_position += 30

	go_back(window, return_function)
	sign_out(window)
