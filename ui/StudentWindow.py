from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window,get_handcursor
from functools import partial

def student_window(student, person, window): #this is personal, only individual can see the whole detail
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	upper_window.create_rectangle(0, 0, 500, 210, fill="#006386",outline = "#006386")
	upper_window.create_text(120,30, fill = "#EBEBE9", font = "Arial 28", text = "Hello There!")
	profile_logo = ImageTk.PhotoImage(file="images/student-w.png")
	upper_window.profile_logo = profile_logo
	upper_window.create_image(250, 80, image=profile_logo)
	upper_window.create_text(250, 180, fill = "#EBEBE9", font = "Arial 10",
					text = "First_name Last_name  \nstudent_number@diemen_academy.nl")
	upper_window.pack()

	def open_student_personal_data(): #confidential data
		window.open_student_personal(window, partial(student_window, student, person),student,person)
	profile_pic = Image.open("images/removed.png")
	profile_pic = profile_pic.resize((42,42), Image.ANTIALIAS)
	personal_image =ImageTk.PhotoImage(profile_pic)
	personal_image.icon = personal_image
	personal_data = Button(window, image = personal_image, command = open_student_personal_data, cursor = get_handcursor())
	personal_data.place(x=20, y = 300, width = 75, height = 75)
	personal_data_text = Button(text = "Personal Data", fg = "#1f3d7a", font="Arial 14",command = open_student_personal_data,cursor = get_handcursor())
	personal_data_text.place(x=90, y = 300, width = 135, height = 75)

	def open_course():
		window.open_student_course(window,partial(student_window, student, person),student,person)
	course_pic = Image.open("images/course.png")
	course_pic = course_pic.resize((42,42), Image.ANTIALIAS)
	course_image =ImageTk.PhotoImage(course_pic)
	course_image.icon = course_image
	course_image_button = Button(window, image = course_image, command = open_course, cursor = get_handcursor())
	course_image_button.place(x=20, y = 370,width = 75, height = 75)
	course_text = Button(window, text = "Courses" , fg = "#1f3d7a" , font="Arial 14", command = open_course, cursor = get_handcursor())
	course_text.place(x=90, y = 370,width = 135, height = 75)

	def open_exam_register():#other teachers can see schedules
		window.open_exam_registration(window,partial(student_window, student, person),student)
	exam_pic = Image.open("images/exam_register.png")
	exam_pic = exam_pic.resize((42,42), Image.ANTIALIAS)
	exam_image =ImageTk.PhotoImage(exam_pic)
	exam_image.icon = exam_image
	exam_image = Button(window, image = exam_image, command = open_exam_register, cursor = get_handcursor())
	exam_image.place(x=20, y = 440,width = 75, height = 75)
	exam_button = Button(window, text = "Examinations", fg = "#1f3d7a",font="Arial 14",  command = open_exam_register, cursor = get_handcursor())
	exam_button.place(x=90, y = 440,width = 135, height = 75)

	def open_counsellor():
		window.open_student_counsellor(window,partial(student_window, student, person),student)
	counsellor_pic = Image.open("images/student_counselor.png")
	counsellor_pic = counsellor_pic.resize((42,42), Image.ANTIALIAS)
	scounsellor_image =ImageTk.PhotoImage(counsellor_pic)
	scounsellor_image.icon = scounsellor_image
	scounsellor_image = Button(window, image = scounsellor_image, command = open_counsellor, cursor = get_handcursor())
	scounsellor_image.place(x=253, y = 300,width = 75, height = 75)
	scounsellor_button = Button(window, text = "Counsellor",fg = "#1f3d7a", font="Arial 14",command = open_counsellor, cursor = get_handcursor())
	scounsellor_button.place(x=320, y = 300,width = 135, height = 75)

	def open_schedule():
		window.open_student_schedule(window,partial(student_window, student, person))
	schedule_pic = Image.open("images/schedule.png")
	schedule_pic = schedule_pic.resize((42,42), Image.ANTIALIAS)
	schedule_image =ImageTk.PhotoImage(schedule_pic)
	schedule_image.icon = schedule_image
	schedule_image = Button(window, image = schedule_image, command = open_schedule, cursor = get_handcursor())
	schedule_image.place(x=253, y = 370,width = 75, height = 75)
	schedule_button = Button(window, text = "Schedule",fg = "#1f3d7a", font="Arial 14",command = open_schedule, cursor = get_handcursor())
	schedule_button.place(x=320, y = 370,width = 135, height = 75)
	#schedule_button1 = Button(window, text = "Schedule", highlightbackground = "green",fg = "#191966", font="Courier 18",height = 3,width = 15, command = open_schedule, cursor = get_handcursor())

	def open_result():
		window.open_student_result(window,partial(student_window, student, person))
	examResult_pic = Image.open("images/exam_result.png")
	examResult_pic = examResult_pic.resize((42,42), Image.ANTIALIAS)
	examResult_image =ImageTk.PhotoImage(examResult_pic)
	examResult_image.icon = examResult_image
	examResult_image = Button(window, image = examResult_image, command = open_result, cursor = get_handcursor())
	examResult_image.place(x=253, y = 440,width = 75, height = 75)
	examResult_button = Button(window, text = "Results",fg = "#1f3d7a", font="Arial 14",height = 2,width = 15, command = open_result, cursor = get_handcursor())
	examResult_button.place(x=320, y = 440,width = 135, height = 75)


"""
	def open_exam():#other teachers can see schedules
		window.open_teacher_schedule(window,student_window)
	schedule_button = Label(window, text = "Exam Registration", font="Courier 18",height = 3,width = 30,
			highlightbackground ="#1a001a",bd = 2, command = open_exam, cursor = get_handcursor())
	schedule_button.place(x=80, y = 455)

	def open_exam_result():#other teachers can see schedules
		window.open_teacher_schedule(window,student_window)
	schedule_button = Label(window, text = "Exam Result", font="Courier 18",height = 3,width = 30,
			highlightbackground ="#1a001a",bd = 2, command = open_exam_result, cursor = get_handcursor())
	schedule_button.place(x=80, y = 455)

"""