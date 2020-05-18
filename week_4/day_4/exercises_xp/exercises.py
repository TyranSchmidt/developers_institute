def favorite_book(title):
	print(f"One of my favorite books is {title}")

favorite_book("The Mind Readers")

# exercise 2

def make_shirt(size, text):
	print(f"We will make your shirt with the size {size} and will have this written on it: {text}")

make_shirt("xl", "I will win")
make_shirt(size = "xl", text = "I will win")

# exercise 3

list = ["Mercurio", "Magnificio", "Amazong", "Releko"]

def show_magicians():
	for i in list:
		print(i)

show_magicians()

# exercise 4

list = ["Mercurio", "Magnificio", "Amazong", "Releko"]

def show_magicians():
	for i in list:
		print(i)

def make_great():
	for i in range(len(list)):
		list[i] += " the Great"

make_great()
show_magicians()

# exercise 5

def checkDriverAge(age = 0):
	if int(age) < 18:
	    print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
	    print("Powering On. Enjoy the ride!");
	elif int(age) == 18:
	    print("Congratulations on your first year of driving. Enjoy the ride!")
	
checkDriverAge()	

