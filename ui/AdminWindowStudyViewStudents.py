from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import askquestion
from ui.AdminWindowStudyViewStudentAdd import view_students_add
from functools import partial
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out

def view_students(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window,text = "Study: ", fg = "#006386", font = "Alice 16 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)

	add_student = Button(window,text = "Add + ",fg = "#006386", font = "Alice 12 bold", highlightbackground = "#006386",command = partial(view_students_add, window, return_function))
	add_student.place(x = 400, y = 100)

	student_name_label = Label(window, text = "Lastname   Firstname", fg = "#e6b800", font="Alice 13 bold",height = 1, width = 25,bg ="#006386")
	student_name_label.place(x=20, y = 140)
	student_id_label = Label(window, text = "Student ID", fg = "#e6b800", font="Alice 13 bold",height = 1, width = 13,bg ="#006386")
	student_id_label.place(x=250, y = 140)	
	action_label = Label(window, text = "Action",fg = "#e6b800", font="Alice 13 bold",height = 1, width = 10,bg ="#006386")
	action_label.place(x=370, y = 140)

	lastname_students = ["abc","def","ghi","jkl","mno"]
	firstname_students = ["mnb","kgb","cni","kpn","zos"]
	id_student= ["12345","22345","32345","42345","52345"]
	num_pos_y = 162
	y_position = 169

	for i in range (len(lastname_students)):

		lastName_label = Label(window, text = lastname_students[i] + "   "  + firstname_students[i],fg = "#00293c", font = "Alice 13", height = 2, width = 25,relief="ridge",borderwidth=2)
		lastName_label.place(x = 20, y = num_pos_y)

		studentID_label = Label(window, text = id_student[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 13,relief="ridge",borderwidth=2)
		studentID_label.place(x = 250 , y = num_pos_y)

		bg_label = Label(window, height = 2, width = 10,relief="ridge",borderwidth=2)
		bg_label.place(x=370, y= num_pos_y)

		def confirm_deletion():
			askquestion(title="Confirmation", message= "Do you want to delete this data?")
		delete_button = Button(window, text = "Delete",font = "Alice 14", fg = "#006386",highlightbackground = "#ffcccc",cursor = "pointinghand", height = 1,width = 5, relief = FLAT, command = confirm_deletion)
		delete_button.place(x= 395, y = y_position)

		num_pos_y += 30
		y_position += 30

	go_back(window, return_function)
	sign_out(window)

