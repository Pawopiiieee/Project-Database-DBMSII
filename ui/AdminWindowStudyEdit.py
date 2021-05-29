from tkinter import *
from tkinter import ttk
import ui.AdminWindowStudies #avoid circular import
from tkinter.messagebox import askquestion
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.SignOut import sign_out

def study_overview_edit(window, return_function,study):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Modify Study", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 140, y = 15)

	study_name = Label(window, text = "Title: ",fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9" )
	study_name.place(x = 20, y = 93)
	input_study = Text(window, height = 1, width = 30, bg = "light yellow", highlightbackground = "#006386", font = "Arial 17")
	input_study.insert(END, study.studyname)
	input_study.place(x=70, y = 90)

	show_desc = Label(window, text = "Description: ",fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9" )
	show_desc.place(x = 20, y = 240)
	input_text = Text(window,  bg = "light yellow", highlightbackground = "#006386", font = "Arial 10")
	input_text.insert(END,study.description)
	input_text.place(x=125, y = 150,height = 220, width = 350)

	language = Label(window, text = "Select a language: ",fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9" )
	language.place(x = 20, y = 420)
	get_language = StringVar()
	selected_language = ttk.Combobox(window,textvariable = get_language, width = 7)
	languages = ["Dutch","English","German"]
	selected_language["value"] = languages
	selected_language.current(languages.index(study.language))
	selected_language.place(x = 170, y = 420)

	amout_year = Label(window, text = "Amount of Years: ",fg = "#006386", font = "Arial 12 bold", bg ="#EBEBE9" )
	amout_year.place(x = 20, y = 470)
	get_total = IntVar()
	amount_years = []
	for i in range(1,11):
		amount_years.append(i)
	total_year = ttk.Combobox(window,textvariable = get_total, width = 7)
	total_year["value"] = amount_years
	total_year.current(amount_years.index(study.studyyears))
	total_year.place(x = 110, y = 470)

	def submit_all():
		result = askquestion(title="Confirmation", message= "Do you want to process?")
		study.studyname = input_study.get(1.0, "end-1c")
		study.description = input_text.get(1.0, "end-1c")
		study.language = get_language.get()
		study.studyyears = get_total.get()
		print(study)
		study.update()
		if result == "yes":
			ui.AdminWindowStudies.admin_window_studies(window, return_function) #avoid circular import
	submit_text = Button(window, text = "Submit",font = "Arial 10 bold",fg = "#006386",highlightbackground ="#48C9B0",height = 2, width = 6, command =submit_all,cursor = get_handcursor())
	submit_text.place(x=200, y = 550)

	go_back(window, return_function)
	sign_out(window)
