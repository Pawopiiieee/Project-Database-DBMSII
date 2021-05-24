from tkinter import *
from tkinter import ttk
import ui.AdminWindowStudies 
from tkinter.messagebox import askquestion 
from ui.Helpers import clear_window, go_back
from ui.SignOut import sign_out
from functools import partial

from model.Study import Study

def create_study(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Create New Study", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 120, y = 15)

	study_name = Label(window, text = "Title: ",fg = "#006386", font = "Alice 15 bold", bg ="#EBEBE9" )
	study_name.place(x = 20, y = 93)
	input_study = Text(window, height = 1, width = 30, bg = "light yellow", highlightbackground = "#006386", font = "Alice 17")
	input_study.place(x=70, y = 90)

	show_desc = Label(window, text = "Description: ",fg = "#006386", font = "Alice 15 bold", bg ="#EBEBE9" )
	show_desc.place(x = 20, y = 240)
	input_text = Text(window, height = 13, width = 33, bg = "light yellow", highlightbackground = "#006386", font = "Alice 15")
	input_text.place(x=125, y = 150)

	language = Label(window, text = "Select a language: ",fg = "#006386", font = "Alice 15 bold", bg ="#EBEBE9" )
	language.place(x = 20, y = 420)
	get_language = StringVar() 
	selected_language = ttk.Combobox(window,textvariable = get_language, width = 7)
	selected_language["value"] = ["Dutch","English","German"]
	selected_language.current(0)
	selected_language.place(x = 170, y = 420)
	""""
	start_year = Label(window, text = "Start Year: ",fg = "#006386", font = "Alice 15 bold", bg ="#EBEBE9" )
	start_year.place(x = 20, y = 450)
	get_year = IntVar()
	year = []
	for i in range (2015,2031):
		year.append(i)
	started_year = ttk.Combobox(window,textvariable = get_year, width = 7)
	started_year["value"] = year
	started_year.current(0)
	started_year.place(x = 110, y = 450)
	"""	
	amout_year = Label(window, text = "Amount of Years: ",fg = "#006386", font = "Alice 15 bold", bg ="#EBEBE9" )
	amout_year.place(x = 20, y = 450)
	get_total = IntVar()
	amount_years = []
	for i in range(1,11):
		amount_years.append(i)
	total_year = ttk.Combobox(window,textvariable = get_total, width = 7)
	total_year["value"] = amount_years
	total_year.current(0)
	total_year.place(x = 160, y = 450)

	def submit_all():
		result = askquestion(title="Confirmation", message= "Do you want to process?")
		get_text = input_text.get(1.0, "end-1c")
		get_study = input_study.get(1.0, "end-1c")
		lang = get_language.get()
		#num_year = get_year.get()
		total_y = get_total.get()
		print(get_text,get_study, lang,total_y)
		if result == "yes":
			study = Study()
			study.studyname = get_study
			study.description = get_text
			study.language = lang
			study.studyyears = total_y
			study.insert()

			ui.AdminWindowStudies.admin_window_studies(window, return_function) #avoid circular import
	
	submit_text = Button(window, text = "Submit",font = "Alice 20 bold",fg = "#006386",highlightbackground ="#48C9B0",height = 2, width = 6, command =submit_all,cursor = "pointinghand")
	submit_text.place(x=200, y = 550)

	go_back(window, return_function)
	sign_out(window)



	

