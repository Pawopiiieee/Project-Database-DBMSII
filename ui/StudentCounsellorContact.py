from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
import ui.StudentCounsellor
from functools import partial

def contact_counsellor(window, return_function): #this is going to show personal data
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	upper_window.create_rectangle(0, 0, 500,70, fill="#006386",outline = "#006386")
	upper_window.pack()
	header_label = Label(window,text = "Student Counsellor", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 100, y = 15)

	counsellorName_label = Label(window,text = "Contact Person: ", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	counsellorName_label.place(x = 20, y = 100)

	counsellorTel_label = Label(window,text = "Phone: ", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	counsellorTel_label.place(x = 20, y = 140)

	counsellorEmail_label = Label(window,text = "Email: ", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	counsellorEmail_label.place(x = 20, y = 180)

	return_course = Button(window,text = "Return", fg = "#2E4053", font = "Arial 12 bold", highlightbackground ="#48C9B0", height = 1,width = 10,borderwidth=2,cursor = get_handcursor(), relief="groove", command = partial(ui.StudentCounsellor.student_personal_counsellor,window, return_function))
	return_course.place(x = 200, y = 550)

	go_back(window, return_function)
	sign_out(window)