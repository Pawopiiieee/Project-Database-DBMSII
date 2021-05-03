from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out


def student_personal_course(window, return_function): #this is going to show personal data
	clear_window(window)
	personal_data_label = Label(window,text = "Course and detail" )
	personal_data_label.place(x=100,y=100)
	go_back(window, return_function)
	sign_out(window)