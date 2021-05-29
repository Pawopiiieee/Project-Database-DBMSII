from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window,get_handcursor

def teacher_window(window): #this is personal, only individual can see the whole detail
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#e9f7fb")
	upper_window.create_rectangle(0, 0, 500, 300, fill="#006386")
	upper_window_text = Label(window,fg = "#e6b800", bg= "#006386", font = "Impact 24", text = "Hello Teacher!")
	upper_window_text.place(x=150,y=25)
	profile_logo = ImageTk.PhotoImage(file="images/icon.png")
	upper_window.profile_logo = profile_logo
	upper_window.create_image(250, 160, image=profile_logo)
	name_text = Label(window, fg = "#e6b800", bg= "#006386", font = "Arial 13", text = "First_name Last_name  \nabc@diemen_academy.nl")
	name_text.place(x=150,y=250)
	upper_window.pack()

	def open_personal_data(): #confidential data
		window.open_teacher_personal(window, teacher_window)
	personal_data_button = Button(window, text = "Personal Data", fg= "#e6b800", font="Courier 18",
			bg="#0f0f3d",highlightbackground ="#0f0f3d",bd = 2, command = open_personal_data, cursor = get_handcursor())
	personal_data_button.place(x=150, y = 325,width = 200, height = 75)
	def open_course():#other teachers can see courses
		window.open_teacher_course(window,teacher_window)
	course_button = Button(window, text = "Courses",fg= "#e6b800", font="Courier 18",height = 3,width = 30,
			bg="#000033",highlightbackground ="#000033",bd = 2,command = open_course, cursor = get_handcursor())
	course_button.place(x=150, y = 390,width = 200, height = 75)
	def open_schedule():#other teachers can see schedules
		window.open_teacher_schedule(window,teacher_window)
	schedule_button = Button(window, text = "Schedule", fg= "#e6b800",font="Courier 18",height = 3,width = 30,
			bg ="#1a001a",highlightbackground ="#1a001a",bd = 2, command = open_schedule, cursor = get_handcursor())
	schedule_button.place(x=150, y = 455,width = 200, height = 75)
"""
	calendar_button = Button(window, text = "Calendar", font="Courier 18",height = 3,width = 30, #other teachers can see calendar
			highlightbackground ="#1a000d",bd = 2, command = calendar)
	calendar_button.place(x=50, y = 500)
"""
