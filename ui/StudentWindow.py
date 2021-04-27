from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window

def student_window(window): #this is personal, only individual can see the whole detail
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#e9f7fb")
	upper_window.create_rectangle(0, 0, 500, 300, fill="#1f1e25")
	upper_window.create_text(120,35, fill = "white", font = "Impact 28", text = "Hello There!")
	profile_logo = ImageTk.PhotoImage(file="images/student-w.png")
	upper_window.profile_logo = profile_logo
	upper_window.create_image(250, 160, image=profile_logo)
	upper_window.create_text(250, 270, fill = "white", font = "Arial 15", 
					text = "First_name Last_name  \nstudent_numberc@diemen_academy.nl")
	upper_window.pack()