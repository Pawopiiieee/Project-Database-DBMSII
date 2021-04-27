from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out


def personal_data(window, return_function): #this is going to show personal data
	clear_window(window)
	personal_data_label = Label(window,text = "Your name, Last name, Birthday, and detail" )
	personal_data_label.place(x=100,y=100)
	go_back(window, return_function)
	sign_out(window)
	
def course(window, return_function):#this is going to show the course the teacher is currently teaching
	clear_window(window)
	course_label = Label(window,text = "Courses and detail" )
	course_label.place(x=100,y=100)
	go_back(window, return_function)
	sign_out(window)
	
def schedule(window, return_function):#this is going to show the schedule for the teacher
	clear_window(window)
	shcedule_label = Label(window,text = "Schedule and detail" )
	shcedule_label.place(x=100,y=100)
	go_back(window, return_function)
	sign_out(window)