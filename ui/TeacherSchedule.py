from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
	
def schedule(window, return_function):#this is going to show the schedule for the teacher
	clear_window(window)
	shcedule_label = Label(window,text = "Schedule and detail" )
	shcedule_label.place(x=100,y=100)
	go_back(window, return_function)
	sign_out(window)