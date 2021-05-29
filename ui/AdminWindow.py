from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from ui.Helpers import clear_window,get_handcursor

def admin_window(window):
	clear_window(window)
	upper_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	upper_window.create_rectangle(0, 0, 500, 210, fill="#e6b800",outline = "#e6b800")
	admin_logo = ImageTk.PhotoImage(file="images/Admin.png")
	upper_window.profile_logo = admin_logo
	upper_window.create_image(250, 100, image=admin_logo)
	upper_window.create_text(250, 180, fill = "#EBEBE9", font = "Arial 20",
					text = "Welcome Admin...")
	upper_window.pack()

	def open_study_data(): #confidential data
		window.open_admin_window_studies(window, admin_window)
	course_pic = Image.open("images/course_admin.png")
	course_pic = course_pic.resize((63,63), Image.ANTIALIAS)
	course_image =ImageTk.PhotoImage(course_pic)
	course_image.icon = course_image
	course_data = Button(window, image = course_image, command = open_study_data, cursor = get_handcursor())
	course_data.place(x=130, y = 250, width = 75, height = 75)
	course_data_text = Button(text = "Studies", fg = "#006386", font="Arial 18 bold", cursor = get_handcursor(), command = open_study_data)
	course_data_text.place(x=205, y = 250, width = 170, height = 75)

	def open_student_data(): #confidential data
		window.open_admin_window_students(window, admin_window)
	student_pic = Image.open("images/student_admin.png")
	student_pic = student_pic.resize((63,63), Image.ANTIALIAS)
	student_image =ImageTk.PhotoImage(student_pic)
	student_image.icon = student_image
	teacher_image = Button(window, image = student_image, command = open_student_data, cursor = get_handcursor())
	teacher_image.place(x=130, y = 350, width = 75, height = 75)
	teacher_data_text = Button(text = "Students", fg = "#00ace6", font="Arial 18 bold", cursor = get_handcursor(), command = open_student_data)
	teacher_data_text.place(x=205, y = 350, width = 170, height = 75)

	def open_teacher_data(): #confidential data
		window.open_admin_window_teachers(window, admin_window)
	teacher_pic = Image.open("images/teacher_admin.png")
	teacher_pic = teacher_pic.resize((63,63), Image.ANTIALIAS)
	teacher_image =ImageTk.PhotoImage(teacher_pic)
	teacher_image.icon = teacher_image
	teacher_image = Button(window, image = teacher_image, command = open_teacher_data, cursor = get_handcursor())
	teacher_image.place(x=130, y = 450, width = 75, height = 75)
	teacher_data_text = Button(text = "Teachers", fg = "#1f1f7a", font="Arial 18 bold", cursor = get_handcursor(), command = open_teacher_data)
	teacher_data_text.place(x=205, y = 450, width = 170, height = 75)
