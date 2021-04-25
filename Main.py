from tkinter import *
from ui.LoadingWindow import loading_screen
from ui.TeacherWindow import teacher_window


if __name__ == "__main__":
	
	master = Tk()
	master.title("Diemen Academy")
	master.geometry("500x700")
	master.resizable(0, 0)

	#loading_screen(master)
	teacher_window(master)
	master.mainloop()