from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window

def teacher_window(window):
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 500)
	upper_window.create_rectangle(0, 0, 500, 300, fill="#1f1e25")
	upper_window.create_text(120,35, fill = "white", font = "Impact 30", text = "Hello Teacher!")
	profile_logo = ImageTk.PhotoImage(file="images/icon.png")
	upper_window.profile_logo = profile_logo
	upper_window.create_image(250, 160, image=profile_logo)
	upper_window.create_text(250, 270, fill = "white", font = "Arial 15", 
					text = "First_name Last_name  \nabc@diemen_academy.nl")
	upper_window.pack()

	personal_data_button = Button(window, text = "Personal Data", font="Courier 18",height = 3,width = 15, 
			highlightbackground ="#0f0f3d",bd = 2, command = window.destroy)
	personal_data_button.place(x=3, y = 305)
	course_button = Button(window, text = "Courses", font="Courier 18",height = 3,width = 15, 
			highlightbackground ="#000033",bd = 2,command = window.destroy)
	course_button.place(x=3, y = 370)
	schedule_button = Button(window, text = "schedule", font="Courier 18",height = 3,width = 15, 
			highlightbackground ="#1a001a",bd = 2, command = window.destroy)
	schedule_button.place(x=3, y = 435)




