from tkinter import *
from ui.LoadingWindow import loading_screen
from ui.LoginWindow import logIn_screen
from ui.TeacherWindow import teacher_window
from ui.StudentWindow import student_window
from ui.TeacherWindowNext import personal_data, course, schedule
from ui.SelectRoleWindow import select_role
from ui.StudentPersonalData import student_personal_data
from ui.StudentCourse import student_personal_course
from ui.StudentSchedule import student_personal_schedule
from ui.StudentCounselor import student_personal_counselor
from ui.StudentExamRegistration import student_exam_registration
from ui.StudentExamResult import student_exam_results

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
	master.open_student_personal = student_personal_data
	master.open_student_course = student_personal_course
	master.open_student_schedule = student_personal_schedule
	master.open_student_counselor = student_personal_counselor
	master.open_exam_registration = student_exam_registration
	master.open_student_exam_result = student_exam_results  

	#loading_screen(master)
	student_window(master)
	#teacher_window(master)
	master.mainloop()