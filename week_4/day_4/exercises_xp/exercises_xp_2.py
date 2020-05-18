def get_age(year, month, day):
	current_year = 2020
	current_month = 4
	current_day = 22
	new_year = current_year - year 
	new_month = current_month - month
	new_day = current_day - day 
	if new_day < 1:
		new_month -= 1
	if new_month < 1:
		new_month += 12
		new_year -= 1
	if new_month in [1, 3, 5, 7, 8, 10, 12]:
		new_day += 31
	elif new_month in [4, 6, 9, 11]:
		new_day += 30
	elif new_month == 2 and new_year%4 == 0:
		new_day += 29
	else:
		new_day += 28	
	return new_year, new_month, new_day

def can_retire(sex, date_of_birth):
	year, month, day = date_of_birth.split("/")
	year = int(year)
	if month[0] == "0":
		month = int(month[1])
	else:
		month = int(month)
	day = int(day)
	new_year, new_month, new_day = get_age(year, month, day)

	if sex == "M" and new_year > 67 or sex == "F" and new_year > 62:
		result = "can"
	elif sex == "M" and new_year == 67 or sex == "F" and new_year == 62:
		if new_month >= 4:
			result = "can"
		else:
			result ="can not"
	else:
		result = "can not"
	return result

sex = input("M/F")
date_of_birth = input("yyyy/mm/dd")

result = can_retire(sex, date_of_birth)

print(f"You {result} retire")

# exercise 2

def make_shirt(size = "large", text = "I love python"):
	print(f"We will make your shirt with the size {size} and will have this written on it: {text}")

make_shirt()
make_shirt("medium")
make_shirt("small", "I love work!")

# exercise 3

def describe_city(city, country = "Israel"):
	print(f"{city} is in {country}.")

describe_city("Tel-aviv")
describe_city("Holon")
describe_city("London")

# exercise 4

def display_message():
	print("We are learning all about Python")

display_message()