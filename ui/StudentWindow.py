from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window

def student_window(window): #this is personal, only individual can see the whole detail
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#1e656d")
	upper_window.create_rectangle(0, 0, 500, 300, fill="#00293c")
	upper_window.create_text(120,35, fill = "white", font = "Impact 28", text = "Hello There!")
	profile_logo = ImageTk.PhotoImage(file="images/student-w.png")
	upper_window.profile_logo = profile_logo
	upper_window.create_image(250, 160, image=profile_logo)
	upper_window.create_text(250, 270, fill = "white", font = "Arial 15", 
					text = "First_name Last_name  \nstudent_number@diemen_academy.nl")
	upper_window.pack()

	def open_student_personal_data(): #confidential data
		window.open_student_personal(window, student_window)
	profile_pic = Image.open("images/removed.png")
	profile_pic = profile_pic.resize((54,54), Image.ANTIALIAS)
	personal_image =ImageTk.PhotoImage(profile_pic)
	personal_image.icon = personal_image
	personal_data = Button(window, image = personal_image, command = open_student_personal_data, cursor = "pointinghand")
	personal_data.place(x=20, y = 370)
	personal_data_text = Button(text = "Personal Data", fg = "#1f3d7a", font="Courier 18",command = open_student_personal_data,height = 3, width = 15, cursor = "pointinghand")
	personal_data_text.place(x=75, y = 370)

	def open_course():
		window.open_student_course(window,student_window)
	course_pic = Image.open("images/course.png")
	course_pic = course_pic.resize((54,54), Image.ANTIALIAS)
	course_image =ImageTk.PhotoImage(course_pic)
	course_image.icon = course_image
	course_image_button = Button(window, image = course_image, command = open_course, cursor = "pointinghand")
	course_image_button.place(x=20, y = 440)
	course_text = Button(window, text = "Courses" , fg = "#1f3d7a" , font="Courier 18",height = 3,width = 15, command = open_course, cursor = "pointinghand")
	course_text.place(x=75, y = 440)

	def open_exam_register():#other teachers can see schedules
		window.open_exam_registration(window,student_window)
	exam_pic = Image.open("images/exam_register.png")
	exam_pic = exam_pic.resize((54,54), Image.ANTIALIAS)
	exam_image =ImageTk.PhotoImage(exam_pic)
	exam_image.icon = exam_image
	exam_image = Button(window, image = exam_image, command = open_exam_register, cursor = "pointinghand")
	exam_image.place(x=20, y = 510)
	exam_button = Button(window, text = "Examinations", fg = "#1f3d7a",font="Courier 18",height = 3,width = 15,  command = open_exam_register, cursor = "pointinghand")
	exam_button.place(x=75, y = 510)

	def open_counselor():
		window.open_student_counselor(window,student_window)
	counselor_pic = Image.open("images/student_counselor.png")
	counselor_pic = counselor_pic.resize((54,54), Image.ANTIALIAS)
	scounselor_image =ImageTk.PhotoImage(counselor_pic)
	scounselor_image.icon = scounselor_image
	scounselor_image = Button(window, image = scounselor_image, command = open_counselor, cursor = "pointinghand")
	scounselor_image.place(x=253, y = 370)
	scounselor_button = Button(window, text = "Counselor",fg = "#1f3d7a", font="Courier 18",height = 3,width = 15, command = open_counselor, cursor = "pointinghand")
	scounselor_button.place(x=308, y = 370)

	def open_schedule():
		window.open_student_schedule(window,student_window)
	schedule_pic = Image.open("images/schedule.png")
	schedule_pic = schedule_pic.resize((54,54), Image.ANTIALIAS)
	schedule_image =ImageTk.PhotoImage(schedule_pic)
	schedule_image.icon = schedule_image
	schedule_image = Button(window, image = schedule_image, command = open_schedule, cursor = "pointinghand")
	schedule_image.place(x=253, y = 440)
	schedule_button = Button(window, text = "Schedule",fg = "#1f3d7a", font="Courier 18",height = 3,width = 15, command = open_schedule, cursor = "pointinghand")
	schedule_button.place(x=308, y = 440)
	#schedule_button1 = Button(window, text = "Schedule", highlightbackground = "green",fg = "#191966", font="Courier 18",height = 3,width = 15, command = open_schedule, cursor = "pointinghand")

	def open_result():
		window.open_student_result(window,student_window)
	examResult_pic = Image.open("images/exam_result.png")
	examResult_pic = examResult_pic.resize((54,54), Image.ANTIALIAS)
	examResult_image =ImageTk.PhotoImage(examResult_pic)
	examResult_image.icon = examResult_image
	examResult_image = Button(window, image = examResult_image, command = open_result, cursor = "pointinghand")
	examResult_image.place(x=253, y = 510)
	examResult_button = Button(window, text = "Results",fg = "#1f3d7a", font="Courier 18",height = 3,width = 15, command = open_result, cursor = "pointinghand")
	examResult_button.place(x=308, y = 510)


"""
	def open_exam():#other teachers can see schedules
		window.open_teacher_schedule(window,student_window)
	schedule_button = Label(window, text = "Exam Registration", font="Courier 18",height = 3,width = 30, 
			highlightbackground ="#1a001a",bd = 2, command = open_exam, cursor = "pointinghand")
	schedule_button.place(x=80, y = 455)

	def open_exam_result():#other teachers can see schedules
		window.open_teacher_schedule(window,student_window)
	schedule_button = Label(window, text = "Exam Result", font="Courier 18",height = 3,width = 30, 
			highlightbackground ="#1a001a",bd = 2, command = open_exam_result, cursor = "pointinghand")
	schedule_button.place(x=80, y = 455)

"""