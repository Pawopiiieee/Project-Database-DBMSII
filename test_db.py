from model.Database import *
from model.Person import *
from model.Student import *
from model.Result import *
from model.Exam import *
from model.Course import *
from model.Teacher import *
from model.Study import * 
import random
import datetime
import itertools

male_name = ["Sem", "Lucas", "Milan", "Daan", "Jayden", "Tim", "Levi", "Thomas", "Thijs", "Jesse", "Luuk", "Stijn", "Ruben", "Lars", "Finn", "Bram", "Julian",
    "Mees", "Sven", "Max", "Gijs", "Noah", "Sam", "Liam", "Luca", "Roan", "Teun", "Tijn", "Nick", "Jan", "Jasper", "Stan", "Daniël", "Floris", "David",
    "Ryan", "Niels", "Tom", "Koen", "Tygo", "Dean", "Robin", "Jens", "Keano", "Mats", "Joep", "Cas", "Willem", "Thijmen", "Dylan", "Hugo", "Justin",
    "Johannes", "Pepijn", "Olivier", "Siem", "Bas", "Mohamed", "Ties", "Timo", "Jurre", "Jelle", "Benjamin", "Damian", "Rayan", "Niek", "Quinten", "Hidde",
    "Guus", "Adam", "Joshua", "Pieter", "Mike", "Mohammed", "Simon", "Pim", "Dani", "Boaz", "Rens", "Joris", "Hendrik", "Vince", "Casper", "Samuel",
    "Wesley", "Wessel", "Mika", "Job", "Alexander", "Jonathan", "Sander", "Rick", "Cornelis", "Twan", "Tobias", "Jason", "Dylano", "Maarten", "Nathan",
    "Tristan"]
female_name = ["Sophie", "Julia", "Emma", "Lotte", "Eva", "Lisa", "Lieke", "Sanne", "Noa", "Anna", "Isa", "Fleur", "Lynn", "Tess", "Sara", "Roos", "Anne", "Maud",
    "Jasmijn", "Femke", "Sarah", "Zoë", "Elin", "Iris", "Anouk", "Naomi", "Amy", "Floor", "Britt", "Evi", "Luna", "Noor", "Nina", "Esmee", "Eline",
    "Amber", "Tessa", "Mila", "Sofie", "Fenna", "Nikki", "Charlotte", "Laura", "Maria", "Vera", "Nienke", "Senna", "Olivia", "Demi", "Bo", "Marit",
    "Elise", "Yara", "Rosalie", "Romy", "Fenne", "Feline", "Fay", "Ilse", "Milou", "Loïs", "Lina", "Sterre", "Isabel", "Liv", "Saar", "Julie", "Fiene",
    "Isabella", "Nora", "Indy", "Puck", "Lara", "Merel", "Mirthe", "Hannah", "Isis", "Isabelle", "Bente", "Esmée", "Robin", "Liz", "Johanna", "Guusje",
    "Jill", "Veerle", "Danique", "Yfke", "Evy", "Meike", "Suze", "Lizzy", "Myrthe", "Quinty", "Benthe", "Madelief", "Emily", "Nova", "Noortje", "Linde"]
last_name = ["Bakker", "Blom", "Boer", "Bos", "Bosch", "Bosman", "Brouwer", "Dekker", "Dijkstra", "Driessen", "Evers", "Gerritsen", "Groen", "Hendriks", "Hermans", "Hoekstra", "Hofman", "Huisman",
    "Jacobs", "Jansen", "Janssen", "Jonker", "Kok", "Koning", "Koster", "Kramer", "Kuijpers", "Kuiper", "Kuipers", "Maas", "Martens", "Meijer", "Mol", "Molenaar", "Mulder", "Peeters",
    "Peters", "Post", "Postma", "Prins", "Sanders", "Schipper", "Scholten", "Schouten", "Smeets", "Smit", "Smits", "Timmermans", "Veenstra", "Verbeek", "Verhoeven", "Vermeulen", "Vink",
    "Visser", "Vos", "Willems", "Willemsen", "Wolters"]

nationality = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian',
    'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian',
    'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti',
    'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese',
    'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian',
    'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese',
    'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican',
    'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian',
    'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian',
    'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander',
    'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian',
    'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']

city_name = ["Amsterdam", "Rotterdam", "Den Haag", "Utrecht", "Eindhoven", "Tilburg", "Groningen", "Almere", "Breda", "Nijmegen", "Enschede", "Apeldoorn", "Haarlem",
    "Amersfoort", "Zaanstad", "Arnhem", "Haarlemmermeer", "'s Hertogenbosch", "Zoetermeer", "Zwolle", "Maastricht", "Leiden", "Dordrecht", "Ede", "Emmen",
    "Westland", "Venlo", "Delft", "Deventer", "Leeuwarden", "Alkmaar", "Sittard-Geleen", "Helmond", "Heerlen", "Hilversum", "Oss", "Amstelveen", "Súdwest-Fryslân",
    "Hengelo", "Purmerend", "Roosendaal", "Schiedam", "Lelystad", "Alphen aan den Rijn", "Leidschendam-Voorburg", "Almelo", "Spijkenisse", "Hoorn", "Gouda",
    "Vlaardingen", "Assen", "Bergen op Zoom", "Capelle aan den IJssel", "Veenendaal", "Katwijk", "Zeist", "Nieuwegein", "Roermond", "Den Helder", "Doetinchem",
    "Hoogeveen", "Terneuzen", "Middelburg"]

study = ["Bussiness ICT","BIM parttime","Mathematical Engineering","Plane design","Precision Engineering","Architecture"]


###
def generatePerson(first_names,last_names,gender,stu_nationality,city,stu):
    person = Person()
    person.fname = random.choice(first_names)
    person.lname =  random.choice(last_names)
    person.gender = gender
    domain = ["gmail.com","hotmail.com","yahoo.com"]
    person.email = person.lname + "_" + person.fname + "@" + random.choice(domain)
    person.full_name = (person.fname, person.lname)
    person.phone_number = "0" + str(random.randint(600000000,699999999))
    start_birthday = datetime.date(1980,1,1)
    end_birthday  = datetime.date(2004,1,1)
    time_between_dates = end_birthday - start_birthday
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    date_of_birth = start_birthday + datetime.timedelta(days=random_number_of_days)

    person.date_of_birth = date_of_birth.strftime('%Y/%m/%d')
    person.dob_password = date_of_birth.strftime("%Y%m%d")
    person.nationality = random.choice(stu_nationality)
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    person.street_name = ''.join(random.choice(alphabets) for _ in range(6))
    person.number = random.randint(100000,200000)
    person.city = random.choice(city)
    person.postal_code = str(random.randint(1111,9999)) + str(''.join(random.choice(alphabets) for _ in range(2)))
    person.stu_program = random.choice(stu)
    person.start_year = random.randint(2015,2020)
    #counselor = ["L. Broglie","M. Planck","L. de Broglie","Planck","B. de Wit"]
    #person.counselor = random.choice(counselor)
    password = person.fname+person.dob_password
    person.password = password
    return person


# Insert a student
#student = Student()
#student.startYear = '2018-05-30'
#student.studyCouncelor = 'N'
#student.personID = 7
#studentID = student.insert()

# Load and modify student object
# student = Student()
# studentID = 1
# student.load(studentID)
# student.personID = 4
# student.update()
#student.delete()
#print(student)
#print(student.getPerson())

#insert a result
# result = Result()
# result.examID = '301'
# result.passed = 'Y'
# result.grade = 7
# result.ResultID = result.insert()

#load and modify result object
# result = Result()
# resultID = 1
# result.load(resultID)
# result.grade = 6
# result.update()

#insert an exam
# exam = Exam()
# exam.coursetitle = 'calculus'
# exam.room = 'ao23'
# exam.resit = 'Y'
# exam.date = '2021-08-09'
# exam.time = '12:00:01'
# exam.courseID = 2
# exam.examID = exam.insert()

#load and modify exam object
# exam = Exam()
# examID = 2
# exam.load(examID)
# exam.room = 'a201'
# exam.update()
# exam.delete()

# course = Course()
# course.coursetitle = 'calculus'
# course.description = 'This course in calculus is intended to develop practical skills in differential and integral calculus'
# course.teacherID = 2
# course.courseID = course.insert()


# Insert a teacher
# teacher = Teacher()
# teacher.salary = 34689
# teacher.studycouncerlor = 'Y'
# teacher.personID = 4
# teacherID = teacher.insert()


# Load and modify teacher object

# teacher = Teacher()
# teacherID = 1
# teacher.load(teacherID)
# teacher.personID = 8
# teacher.update()
# print(teacher)
# print(teacher.getPerson())


#insert a study
study = Study()
study.studyname = "Mathematical Engineering"
study.description = "Learn math & code"
study.language = "EN"
study.studyyears = 4
studyID = study.insert()


#for i in range (1):
#    boy_name = generatePerson(male_name,last_name,"M", nationality,city_name,study)
#    boy_name.insert();
#    print(boy_name)

#for i in range (1):
#	girl_name = generatePerson(female_name,last_name,"F", nationality,city_name,study)
#	print(girl_name)
