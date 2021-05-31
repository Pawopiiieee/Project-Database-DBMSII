from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out
from ui.StudentCounsellorContact import contact_counsellor
from functools import partial

def student_personal_counsellor(window, return_function, student): #this is going to show personal data
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	upper_window.create_rectangle(0, 0, 500,70, fill="#006386",outline = "#006386")
	upper_window.pack()
	header_label = Label(window,text = "Student Counsellor", fg = "#EBEBE9", font = "Arial 30", bg ="#006386")
	header_label.place(x = 100, y = 15)

	explanation_label = Label(window,
	text = "You can contact us for a confidential conversation to help you with support,\nadvice and information on the following matters.",
	fg = "#006386", font = "Arial 10", bg ="#EBEBE9", justify = "left")
	explanation_label.place(x = 10, y = 90)

	special_circumstances_button = Button(window, text = "Special Circumstances", fg = "#1f3d7a", font="Arial 10 bold",height = 1,width = 25, cursor = get_handcursor(),command = partial(contact_counsellor,window,return_function, student))
	special_circumstances_button.place(x = 50, y = 150)
	special_circumstances_label = Label(window,text = "-Family Circumstance \n-Illness \n-Study Delay \n-Registration and Deregistration",
	fg = "#006386", font = "Arial 10", bg ="#EBEBE9",justify = "left")
	special_circumstances_label.place(x= 50, y = 210)

	financial_problem_button = Button(window, text = "Financial Problems", fg = "#1f3d7a", font="Arial 10 bold",height = 1,width = 25, cursor = get_handcursor(),command = partial(contact_counsellor,window,return_function, student))
	financial_problem_button.place(x = 50, y = 300)
	financial_problem_label = Label(window,text = "-Applying for financial compensation in case of study delay \n-When you are not (or no longer) eligible for student finance \nand loans provided by the Dutch government or need advice \nor information about their student finance",
	fg = "#006386", font = "Arial 10", bg ="#EBEBE9",justify = "left")
	financial_problem_label.place(x= 50, y = 360)

	disability_button = Button(window, text = "Study with a Disability or a Chronic Illness", fg = "#1f3d7a", font="Arial 10 bold",height = 1,width = 35, cursor = get_handcursor(),command = partial(contact_counsellor,window,return_function, student))
	disability_button.place(x = 50, y = 455)
	disability_label = Label(window,text = "-Studying with a disability \n-Applying for educational facilities due to a physical/mental illness ",
	fg = "#006386", font = "Arial 10", bg ="#EBEBE9",justify = "left")
	disability_label.place(x= 50, y = 510)




	go_back(window, return_function)
	sign_out(window)