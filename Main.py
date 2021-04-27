from tkinter import *
from ui.LoadingWindow import loading_screen
from ui.LoginWindow import logIn_screen
from ui.TeacherWindow import teacher_window
from ui.StudentWindow import student_window
from ui.TeacherWindowNext import personal_data, course, schedule
from ui.SelectRoleWindow import select_role

if __name__ == "__main__":
	
	master = Tk()
	master.title("Diemen Academy")
	master.geometry("500x700")
	master.resizable(0, 0)

	master.open_login = logIn_screen
	master.open_select_role = select_role
	master.open_teacher = teacher_window
	master.open_teacher_personal = personal_data
	master.open_teacher_course = course
	master.open_teacher_schedule = schedule
	master.open_student = student_window

	#loading_screen(master)
	student_window(master)
	#teacher_window(master)
	master.mainloop()