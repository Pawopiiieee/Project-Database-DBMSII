from tkinter import *
from tkinter import ttk
from ui.Helpers import clear_window, go_back,get_handcursor
from tkinter.messagebox import showinfo,askquestion
from ui.SignOut import sign_out
from functools import partial
import ui.AdminWindowStudents
import datetime
from model.Person import *
from model.Student import *
from model.Teacher import *
from model.Study import *

def createNew_student(window, return_function):
	clear_window(window)
	whole_window = Canvas(window, width = 500, height = 700, bg = "#EBEBE9")
	whole_window.create_rectangle(0, 0, 500, 70, fill="#006386", outline = "#006386")
	whole_window.pack()
	header_label = Label(window,text = "Create New Student", fg = "#e6b800", font = "Arial 30", bg ="#006386")
	header_label.place(x = 75, y = 15)

	lastname_label = Label(window,text = "Lastname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	lastname_label.place(x = 20, y = 100)
	input_lastname = Text(window, height = 1, width = 14, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_lastname.place(x=100, y = 100)

	firstname_label = Label(window,text = "Firstname", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	firstname_label.place(x = 250, y = 100)
	input_firstname = Text(window, height = 1, width = 14, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_firstname.place(x=330, y = 100)

	studentID_label = Label(window,text = "Student ID", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	studentID_label.place(x = 20, y = 130)
	input_studentID = Text(window, height = 1, width = 14, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_studentID.place(x=100, y = 130)

	startYear = IntVar()
	start_Year = []
	for i in range(2010,2022):
		start_Year.append(i)
	start_Year_sh = ttk.Combobox(window,textvariable = startYear, width = 5)
	start_Year_sh["value"] = start_Year
	start_Year_sh["state"] = "readonly"
	def start_Year_choose (event):
		confirm_msg = f"You Selected {start_Year_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	start_Year_sh.bind("<<ComboboxSelected>>", start_Year_choose)
	start_Year_sh.place(x = 330, y = 130)
	startYear_label = Label(window,text = "Start Year", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	startYear_label.place(x = 250, y = 130)

	selected_study = StringVar()
	studies = Study.load_all()
	studynames = []
	for study in studies:
		studynames.append(study.studyname)
	study_sh = ttk.Combobox(window,textvariable = selected_study,width = 20)
	study_sh["value"] = studynames
	study_sh["state"] = "readonly"
	def study_changed (event):
		confirm_msg = f"You Selected {study_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	study_sh.bind("<<ComboboxSelected>>", study_changed)
	study_sh.place(x = 80, y = 160)
	study_label = Label(window,text = "Study", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	study_label.place(x = 20, y = 160)

	selected_counsellor = StringVar()
	counsellors = Teacher.load_studycounselers()
	counsellornames = []
	for c in counsellors:
		person = c.getPerson()
		counsellornames.append(person.fname + " " + person.lname)
	counsellor_sh = ttk.Combobox(window,textvariable = selected_counsellor,width = 20)
	counsellor_sh["value"] = counsellornames
	counsellor_sh["state"] = "readonly"

	def counsellor_changed (event):
		confirm_msg = f"You Selected {counsellor_sh.get()}!"
		showinfo(title="Result", message= confirm_msg)
	counsellor_sh.bind("<<ComboboxSelected>>", counsellor_changed)
	counsellor_sh.place(x = 170, y = 190)
	studentCounsellor_label = Label(window, text = "Student Counsellor",fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9" )
	studentCounsellor_label.place(x = 20, y = 190)

	personal_label = Label(window,text = "Personal Detail", fg = "#e6b800", font = "Arial 12 bold", bg ="#006386")
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
	studentCounsellor_label = Label(window, text = "Nationality",fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9" )
	studentCounsellor_label.place(x = 20, y = 320)

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
	studentCounsellor_label.place(x = 20, y = 350)

	houseNo_label = Label(window,text = "House No.", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	houseNo_label.place(x = 20, y = 380)
	input_houseNo = Text(window, height = 1, width = 5, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_houseNo.place(x=100, y = 380)
	input_houseNo2 = Text(window, height = 1, width = 3, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_houseNo2.place(x=160, y = 380)

	street_label = Label(window,text = "Street", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	street_label.place(x = 210, y = 380)
	input_street = Text(window, height = 1, width = 20, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_street.place(x=270, y = 380)

	city_label = Label(window,text = "City", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	city_label.place(x = 20, y = 410)
	input_city = Text(window, height = 1, width = 20, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_city.place(x=70, y = 410)

	postal_label = Label(window,text = "Postal Code", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	postal_label.place(x = 270, y = 410)
	input_postal = Text(window, height = 1, width = 6, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_postal.place(x=360, y = 410)
	input_postal2 = Text(window, height = 1, width = 3, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_postal2.place(x=430, y = 410)

	phoneNumber_label = Label(window,text = "Phone Number", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	phoneNumber_label.place(x = 20, y = 440)
	input_phoneNumber = Text(window, height = 1, width = 15, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_phoneNumber.place(x=140, y = 440)

	email_label = Label(window,text = "Email", fg = "#006386", font = "Arial 10 bold", bg ="#EBEBE9")
	email_label.place(x = 20, y = 470)
	input_email = Text(window, height = 1, width = 25, bg = "light yellow", highlightbackground = "#006386", font = "Arial 13")
	input_email.place(x=80, y = 470)

	def submit_all():
		result = askquestion(title="Confirmation", message= "Do you want to process?")

		if result == "yes":
			person = Person()
			person.lname = input_lastname.get(1.0, "end-1c")
			person.fname = input_firstname.get(1.0, "end-1c")
			person.birthday = datetime.date(birthYear.get(), months.index(birthMonth.get()) + 1, birthDay.get())
			person.nationality = selected_nationality.get()
			person.gender = selected_gender.get()
			person.streetNumber = str(input_houseNo.get(1.0, "end-1c")) + str(input_houseNo2.get(1.0, "end-1c"))
			person.streetname = input_street.get(1.0, "end-1c")
			person.city = input_city.get(1.0, "end-1c")
			person.postalCode = str(input_postal.get(1.0, "end-1c")) + str(input_postal2.get(1.0, "end-1c"))
			person.phone = input_phoneNumber.get(1.0, "end-1c")
			person.email = input_email.get(1.0, "end-1c")
			person.insert()

			student = Student()
			student.personID = person.personID
			student.studentID = int(input_studentID.get(1.0, "end-1c"))
			student.startYear = datetime.date(startYear.get(), 1, 1)
			student.enrolled = selected_study.get()
			counseler_index = counsellornames.index(selected_counsellor.get())
			student.studyCouncelor = counsellors[counseler_index].teacherID
			student.insert()

			person.userName = (person.lname + str(student.studentID))
			person.userPass = "welkom01"
			person.update()
		
			ui.AdminWindowStudents.admin_window_students(window, return_function) #avoid circular import

	submit_text = Button(window, text = "Submit",font = "Arial 10  bold",fg = "#006386",highlightbackground ="#48C9B0",height = 1, width = 6, command =submit_all,cursor = get_handcursor())
	submit_text.place(x=200, y = 530)

	go_back(window, return_function)
	sign_out(window)