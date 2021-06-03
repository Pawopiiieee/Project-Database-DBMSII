from model.Database import *
from model.Person import *
from model.Student import *
from model.Result import *
from model.Exam import *
from model.Course import *
from model.Teacher import *
from model.Study import *
from model.Admin import *
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

study_names = ["Bussiness ICT","BIM parttime","Mathematical Engineering","Plane design","Precision Engineering","Architecture"]
course_name = ["Computational Thinking","Computer Networks","Linear Algebra","Logic and Modelling","Biological Psychology","Data Wrangling"]

def getRandomDate(startYear, endYear):
    start_day = datetime.date(startYear,1,1)
    end_day  = datetime.date(endYear,1,1)
    time_between_dates = end_day - start_day
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return (start_day + datetime.timedelta(days=random_number_of_days))

###

def generateStudy(name):
    study = Study()
    study.studyname = name
    study.description = ("Welcome to " + name)
    study.language = random.choice(["Dutch", "English", "German"])
    study.studyyears = random.randint(1, 6)
    study.insert()
    return study


studies = []
for s in study_names:
    studies.append(generateStudy(s))

def generatePerson():
    person = Person()
    person.gender = random.choice(['M', 'F', 'O'])
    if (person.gender == 'F'):
        person.fname = random.choice(female_name)
    else:
        person.fname = random.choice(male_name)
    person.lname =  random.choice(last_name)
    domain = ["gmail.com","hotmail.com","yahoo.com"]
    person.email = person.lname + "_" + person.fname + "@" + random.choice(domain)
    person.phone = "0" + str(random.randint(600000000,699999999))
    person.birthday = getRandomDate(1980, 2004)
    person.nationality = random.choice(nationality)
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    person.streetname = ''.join(random.choice(alphabets) for _ in range(6))
    person.streetNumber = random.randint(100000,200000)
    person.city = random.choice(city_name)
    person.postalCode = str(random.randint(1111,9999)) + str(''.join(random.choice(alphabets) for _ in range(2)))
    person.insert()
    return person

def generateTeacher(is_admin = False):
    person = generatePerson()

    teacher = Teacher()
    teacher.salary = random.randint(2500, 6500)
    teacher.studycouncelor = random.choice(['Y', 'N'])
    teacher.personID = person.personID
    teacher.insert()
    
    if is_admin:
        person.userName = "admin"
    else:
        person.userName = (person.lname + str(teacher.teacherID))
    person.userPass = "welkom01"
    person.update()
    return teacher

teachers = []
counselers = []
for i in range(4):
    t = generateTeacher()
    if i == 0:
        # ensure there is always at least 1 studycounseler
        t.studycouncelor = 'Y'
        t.update()
    teachers.append(t)
    if (t.studycouncelor == 'Y'):
        counselers.append(t)
        
def generateCourse(name):
    course = Course()
    course.coursetitle = name
    course.description = ("Welcome to the course of " + name)
    course.credits = random.randint(1, 5)
    course.studyID = random.choice(studies).studyID
    course.teacherID = random.choice(teachers).teacherID
    course.insert()

    exam = Exam()
    exam.courseID = course.courseID
    exam.date = getRandomDate(2020, 2022)
    exam.resit = random.choice(['Y', 'N'])
    exam.room = random.randint(1777, 2000)
    return course

courses = []
for c in course_name:
    courses.append(generateCourse(c))

def generateStudent():
    person = generatePerson()

    student = Student()
    student.startYear = datetime.date(random.randint(2012, 2024), 1, 1)
    student.studyCouncelor = random.choice(counselers).teacherID
    student.enrolled = random.choice(studies).studyname
    student.personID = person.personID
    student.insert()
    
    person.userName = (person.lname + str(student.studentID))
    person.userPass = "welkom01"
    person.update()
    return student
    
students = []
for i in range(25):
    students.append(generateStudent())


def generateAdmin():
    person = generateTeacher(True)

    admin = Admin()
    admin.personID = person.personID
    admin.insert()

generateAdmin()