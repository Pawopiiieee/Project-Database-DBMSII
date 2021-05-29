from tkinter import *
from tkinter import ttk
from ui.Helpers import clear_window, go_back,get_handcursor
import ui.AdminWindowStudyViewStudents
from tkinter.messagebox import askquestion,showerror
from ui.SignOut import sign_out

def view_students_add(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Study Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 140, y = 15)

	title_label = Label(window,text = "Study: ", fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9")
	title_label.place(x = 20, y = 100)


	student_id = Label(window, text = "Student ID",fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9" )
	student_id.place(x = 20, y = 130)
	input_id = Text(window, height = 1, width = 25, bg = "light yellow", highlightbackground = "#006386", font = "Arial 17")
	input_id.place(x=130, y = 130)

	id_student= [12345,22345,32345,42345,52345,1129,992776]

	def submit_data():
		get_id = input_id.get(1.0, "end-1c")

		if int(get_id) not in id_student:
			showerror(title="Error", message= "Student ID not found!",icon ="error")
		else:
			result = askquestion(title="Confirmation", message= "Do you want to proceed?")
			if result == "yes":
				print (get_id)
				ui.AdminWindowStudyViewStudents.view_students(window, return_function)


	submit_text = Button(window, text = "Submit",font = "Arial 14 bold",fg = "#006386",bg="#48C9B0",highlightbackground ="#48C9B0",command =submit_data,cursor = get_handcursor())
	submit_text.place(x=180, y = 300, width = 150,height = 30)







	go_back(window, return_function)
	sign_out(window)