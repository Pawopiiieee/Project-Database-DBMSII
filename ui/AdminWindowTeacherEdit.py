from tkinter import *
from tkinter import ttk
from ui.Helpers import clear_window, go_back,get_handcursor
from ui.AdminWindowTeacherAddEditCourses import teacher_edit_courses
from tkinter.messagebox import showinfo,askquestion
from ui.SignOut import sign_out
from functools import partial
import ui.AdminWindowTeacherView
from model.Person import *
from model.Student import *
from model.Teacher import *
from model.Study import *
import datetime

def teacher_edit(window, return_function,teacher, person):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Teacher Overview", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 100, y = 15)

	lastname_label = Label(window,text = "Lastname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	lastname_label.place(x = 20, y = 100)
	input_lastname = Text(window, height = 1, width = 14, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_lastname.insert(END, person.lname)
	input_lastname.place(x=100, y = 100)

	firstname_label = Label(window,text = "Firstname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	firstname_label.place(x = 250, y = 100)
	input_firstname = Text(window, height = 1, width = 14, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_firstname.insert(END, person.fname)
	input_firstname.place(x=330, y = 100)

	teacherID_label = Label(window,text = "Teacher ID", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	teacherID_label.place(x = 20, y = 130)
	input_teacherID = Text(window, height = 1, width = 14, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_teacherID.insert(END, teacher.teacherID)
	input_teacherID.place(x=100, y = 130)

	salary_label = Label(window,text = "Salary", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	salary_label.place(x = 250, y = 130)
	input_salary = Text(window, height = 1, width = 14, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_salary.insert(END, teacher.salary)
	input_salary.place(x=330, y = 130)

	selected_counsellor = StringVar()
	counsellors = ["Y", "N"]
	counsellor_sh = ttk.Combobox(window,textvariable = selected_counsellor,width = 4)
	counsellor_sh["value"] = counsellors
	counsellor_sh["state"] = "readonly"
	def counsellor_changed (event):
		confirm_msg = f"You Selected {counsellor_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	counsellor_sh.bind("<<ComboboxSelected>>", counsellor_changed)
	counsellor_sh.place(x = 120, y = 160)
	studentCounsellor_label = Label(window, text = "Student Counsellor",fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9" )
	counsellor_sh.current(counsellors.index(teacher.studycouncelor))
	studentCounsellor_label.place(x = 20, y = 160)

	courses_button = Button(window, text = "Add/Remove Courses",font = "Arial 10 bold",fg = "#006386",highlightbackground ="#29B6F6",height = 1, width = 18,cursor = get_handcursor(),command = partial(teacher_edit_courses,window, return_function,teacher, person))
	courses_button.place(x = 170, y = 190)

	personal_label = Label(window,text = "Personal Detail", fg = "#e6b800", font = "Arial 18 bold", bg ="#006386")
	personal_label.place(x = 20, y = 240)

	birthYear = IntVar()
	birth_year = []
	for i in range(1950,2011):
		birth_year.append(i)
	birth_year_ch = ttk.Combobox(window,textvariable = birthYear, width = 7)
	birth_year_ch["value"] = birth_year
	birth_year_ch["state"] = "readonly"
	def birth_year_choose (event):
		confirm_msg = f"You Selected {birth_year_ch.get()}!"
		showinfo(title="Result", message= confirm_msg)
	birth_year_ch.bind("<<ComboboxSelected>>", birth_year_choose)
	birth_year_ch.current(birth_year.index(person.birthday.year))
	birth_year_ch.place(x = 210, y = 290)

	birthMonth = StringVar()
	months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"Septembr",
	"October",
	"November",
	"December"
	]
	birth_month_ch = ttk.Combobox(window,textvariable = birthMonth, width = 10)
	birth_month_ch["value"] = months
	birth_month_ch["state"] = "readonly"
	birth_month_ch.place(x = 300, y = 290)
	def birth_month_choose (event):
		confirm_msg = f"You Selected {birth_month_ch.get()}!"
		showinfo(title="Result", message= confirm_msg)
	birth_month_ch.bind("<<ComboboxSelected>>", birth_month_choose)
	birth_month_ch.current(person.birthday.month - 1)

	birthDay = IntVar()
	birth_day = []
	for i in range(1,32):
		birth_day.append(i)
	birth_day_ch = ttk.Combobox(window,textvariable = birthDay, width = 3)
	birth_day_ch["value"] = birth_day
	birth_day_ch["state"] = "readonly"
	def birth_day_choose (event):
		confirm_msg = f"You Selected {birth_day_ch.get()}!"
		showinfo(title="Result", message= confirm_msg)
	birth_day_ch.bind("<<ComboboxSelected>>", birth_day_choose)
	birth_day_ch.place(x = 420, y = 290)
	dob_label = Label(window,text = "Date of Birth (YY/MM/DD)", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	birth_day_ch.current(birth_day.index(person.birthday.day))
	dob_label.place(x = 20, y = 290)

	selected_nationality = StringVar()
	nationalities = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']
	nationality = ttk.Combobox(window,textvariable = selected_nationality,width = 15)
	nationality["value"] = nationalities
	nationality["state"] = "readonly"
	def nationality_changed (event):
		confirm_msg = f"You Selected {nationality.get()}!"
		showinfo(title="Result", message= confirm_msg)
	nationality.bind("<<ComboboxSelected>>", nationality_changed)
	nationality.place(x = 120, y = 320)
	nationality_label = Label(window, text = "Nationality",fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9" )
	nationality.current(nationalities.index(person.nationality))
	nationality_label.place(x = 20, y = 320)

	selected_gender = StringVar()
	genders = ["M","F","O"]
	gender_sh = ttk.Combobox(window,textvariable = selected_gender,width = 10)
	gender_sh["value"] = genders
	gender_sh["state"] = "readonly"
	def counsellor_changed (event):
		confirm_msg = f"You Selected {gender_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	gender_sh.bind("<<ComboboxSelected>>", counsellor_changed)
	gender_sh.place(x = 100, y = 350)
	studentCounsellor_label = Label(window, text = "Gender",fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9" )
	gender_sh.current(genders.index(person.gender))
	studentCounsellor_label.place(x = 20, y = 350)

	houseNo_label = Label(window,text = "House No.", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	houseNo_label.place(x = 20, y = 380)
	input_houseNo = Text(window, height = 1, width = 5, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_houseNo.insert(END, (str(person.streetNumber)))
	input_houseNo.place(x=100, y = 380)

	street_label = Label(window,text = "Street", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	street_label.place(x = 210, y = 380)
	input_street = Text(window, height = 1, width = 20, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_street.insert(END, (str(person.streetname)))
	input_street.place(x=270, y = 380)

	city_label = Label(window,text = "City", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	city_label.place(x = 20, y = 410)
	input_city = Text(window, height = 1, width = 20, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_city.insert(END, (str(person.city)))
	input_city.place(x=70, y = 410)

	postal_label = Label(window,text = "Postal Code", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	postal_label.place(x = 270, y = 410)
	input_postal = Text(window, height = 1, width = 6, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_postal.insert(END, (person.postalCode))
	input_postal.place(x=360, y = 410)

	phoneNumber_label = Label(window,text = "Phone Number", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	phoneNumber_label.place(x = 20, y = 440)
	input_phoneNumber = Text(window, height = 1, width = 15, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_phoneNumber.insert(END, (person.phone))
	input_phoneNumber.place(x=140, y = 440)

	email_label = Label(window,text = "Email", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	email_label.place(x = 20, y = 470)
	input_email = Text(window, height = 1, width = 15, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_email.insert(END, (person.email))
	input_email.place(x=80, y = 470)

	def submit_all():
		result = askquestion(title="Confirmation", message= "Do you want to process?")
		if result == "yes":
			person.lname = input_lastname.get(1.0, "end-1c")
			person.fname = input_firstname.get(1.0, "end-1c")
			person.birthday = datetime.date(birthYear.get(), months.index(birthMonth.get()) + 1, birthDay.get())
			person.nationality = selected_nationality.get()
			person.gender = selected_gender.get()
			person.streetNumber = str(input_houseNo.get(1.0, "end-1c")) 
			person.streetname = input_street.get(1.0, "end-1c")
			person.city = input_city.get(1.0, "end-1c")
			person.postalCode = str(input_postal.get(1.0, "end-1c")) 
			person.phone = input_phoneNumber.get(1.0, "end-1c")
			person.email = input_email.get(1.0, "end-1c")
			person.update()

			teacher.teacherID = int(input_teacherID.get(1.0, "end-1c"))
			teacher.salary = int(input_salary.get(1.0, "end-1c"))
			teacher.studyCouncelor = selected_counsellor.get()
			teacher.update()
		
			ui.AdminWindowTeacherView.teacher_view(window, return_function,teacher,person) #avoid circular import

	submit_text = Button(window, text = "Submit",font = "Arial 10  bold",fg = "#006386",highlightbackground ="#48C9B0",height = 1, width = 6, command =submit_all,cursor = get_handcursor())
	submit_text.place(x=200, y = 530)
	go_back(window, return_function)
	sign_out(window)