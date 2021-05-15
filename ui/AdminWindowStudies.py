from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  
from ui.Helpers import clear_window, go_back
from ui.AdminWindowStudyEdit import study_overview_edit
from ui.AdminWindowStudyView import study_over_view
from ui.SignOut import sign_out
from functools import partial


def admin_window_studies(window,return_function): 
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "An Overview", fg = "#e6b800", font = "Alice 35", bg ="#006386")
	header_label.place(x = 150, y = 15)

	create_data_text = Button(text = "Create new studies", fg = "#e6b800", font="Alice 12",height = 2, width = 15, cursor = "pointinghand", highlightbackground =  "#006386")
	create_data_text.place(x=20, y = 80)

	header_label1 = Label(window, text = "#",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 3,bg ="#006386")
	header_label1.place(x=10, y = 120)
	header_label2 = Label(window, text = "Title",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 15,bg ="#006386")
	header_label2.place(x=40, y = 120)
	header_label3 = Label(window, text = "Description",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 15,bg ="#006386" )
	header_label3.place(x=180, y = 120)
	header_label4 = Label(window, text = "Action",fg = "#e6b800", font="Alice 13 bold",height = 2, width = 18,bg ="#006386" )
	header_label4.place(x=320, y = 120)

	studies = ["abc","def","ghi","jkl","mno"]
	descriptions = ["abcdefghi","abcdefghi","abcdefghi","abcdefghi","abcdefghi"]
	num_pos_y = 158
	#initial_num = 0
	y_position = 165
	for i in range (len(studies)):
		number_label = Label(window, text = (i + 1),fg = "#00293c", font = "Alice 13", height = 2, width = 3 )
		number_label.place(x = 10, y = num_pos_y)
		#initial_num += 1
		course_label = Label(window, text = studies[i],fg = "#00293c", font = "Alice 13", height = 2, width = 15)
		course_label.place(x = 40, y = num_pos_y)

		desc_label = Label(window, text = descriptions[i],fg = "#00293c", font = "Alice 13",  height = 2, width = 15)
		desc_label.place(x = 180 , y = num_pos_y)

		bg_label = Label(window, height = 2, width = 18)
		bg_label.place(x=320, y= num_pos_y)
		num_pos_y += 30

		view_button = Button(window, text = "View",font = "Alice 14", fg = "#006386",highlightbackground = "#ccd9ff",cursor = "pointinghand", height = 1,width = 4, relief = FLAT,command = partial(study_over_view, window, return_function))
		view_button.place(x= 330, y = y_position)
	
		edit_button = Button(window, text = "Edit",font = "Alice 14", fg = "#006386",highlightbackground = "#fff2cc",cursor = "pointinghand", height = 1,width = 4, relief = FLAT,command = partial(study_overview_edit, window, return_function))
		edit_button.place(x= 380, y = y_position)
		delete_button = Button(window, text = "Delete",font = "Alice 14", fg = "#006386",highlightbackground = "#ffcccc",cursor = "pointinghand", height = 1,width = 5, relief = FLAT)
		delete_button.place(x= 430, y = y_position)
		y_position += 30

	go_back(window, return_function)
	sign_out(window)

"""
	create_pic = Image.open("images/create-w.png")
	create_pic = create_pic.resize((30,30), Image.ANTIALIAS)
	create_image =ImageTk.PhotoImage(create_pic)
	create_image.icon = create_image
	create_data = Button(window, image = create_image, cursor = "pointinghand")
	create_data.place(x=20, y = 80)
"""
