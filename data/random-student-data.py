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

class Student:
	first_name = None
	last_name = None
	date_of_birth = None
	nationality = None
	gender = None
	street = None
	city = None
	postal_code = None
	phone_number = None
	email = None
	student_number = None
	study_program = None
	start_year = None
	counselor = None

	def __repr__(self):
		return str(self.__dict__)

def full_name(first_names,last_names,gender,stu_nationality,city,stu):
	student = Student()
	student.first_name = random.choice(first_names)
	student.last_name =  random.choice(last_names)
	student.gender = gender
	domain = ["gmail.com","hotmail.com","yahoo.com"]
	student.email = student.last_name + "_" + student.first_name + "@" + random.choice(domain)
	student.full_name = (student.first_name, student.last_name)
	student.phone_number = "0" + str(random.randint(600000000,699999999))
	start_birthday = datetime.date(1980,1,1)
	end_birthday  = datetime.date(2004,1,1)
	time_between_dates = end_birthday - start_birthday
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	date_of_birth = start_birthday + datetime.timedelta(days=random_number_of_days)
	student.date_of_birth = date_of_birth.strftime('%Y/%m/%d')
	student.nationality = random.choice(stu_nationality)
	alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	student.street_name = ''.join(random.choice(alphabets) for _ in range(6))
	student.number = random.randint(100000,200000)
	student.city = random.choice(city)
	student.postal_code = str(random.randint(1111,9999)) + str(''.join(random.choice(alphabets) for _ in range(2)))
	student.stu_program = random.choice(stu)
	student.start_year = random.randint(2015,2020)
	counselor = ["L. Broglie","M. Planck","L. de Broglie","Planck","B. de Wit"]
	student.counselor = random.choice(counselor)

	return student


for i in range (50):
	boy_name = full_name(male_name,last_name,"M", nationality,city_name,study)
	print(boy_name)

for i in range (50):
	girl_name = full_name(girl_name,last_name,"F", nationality,city_name,study)
	print(girl_name)



