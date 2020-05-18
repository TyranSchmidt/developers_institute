class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Mittens", 3)
cat2 = Cat("Mayo", 6)
cat3 = Cat("Reya", 4)

def find_oldest():
	ages = [cat1.age, cat2.age, cat3.age]
	ages.sort(reverse = True)
	print(f"The oldest cat is {ages[0]} years old.")

find_oldest()	

# exercise 2

class Dog():
	def __init__(self, nameDog, heightDog):
		self.name = nameDog
		self.height = heightDog

	def talk(self):
		print("Wouaf")
	def jump(self):
		print(self.height*2)

Davids_dog = Dog("Rex", 50)
Davids_dog.talk()
Davids_dog.jump()

Sarahs_dog = Dog("Teacup", 20)
Sarahs_dog.talk()
Sarahs_dog.jump()

def bigger_dog(Rex_height = 50, Teacup_height = 20):
	if Rex_height > Teacup_height:
		print("Rex is bigger than Teacup")
	elif Teacup_height > Rex_height:
		print("Teacup is bigger than Rex")

bigger_dog()
Davids_dog.winner = True
Sarahs_dog.winner = False

# exercise 3

class Zoo():
	def __init__(self, zooName):
		self.animals = []
		self.name = zooName
	def add_animal(self, new_animal):
			if new_animal not in self.animals:
				self.animals.append(new_animal)

new_zoo = Zoo("Exotic Friends")
new_zoo.add_animal("zebra")
new_zoo.add_animal("arbez")
def get_animals():
	print(", ".join(new_zoo.animals))

get_animals()

def sell_animal(animal_sold):
	print(f"goodbye {animal_sold}")
	new_zoo.animals.remove(animal_sold)

sell_animal("zebra")

new_zoo.add_animal("zebra")
new_zoo.add_animal("abc")
new_zoo.add_animal("anaconda")
new_zoo.add_animal("bbc")
print(new_zoo.animals)

def sort_animal():
	zoo_animals = new_zoo.animals
	zoo_animals.sort()	
	full_list = []
	animals_dict = {}
	temp = []
	for animals in zoo_animals:
		if len(temp) > 0:
			if temp[0][0] == animals[0]:
				temp.append(animals)
				if zoo_animals[-1] == animals:
					full_list.append(temp)
			else:
				if len(temp) > 1:
					full_list.append(temp)
					temp = []
					temp.append(animals)
					if zoo_animals[-1] == animals:
						full_list.append(temp[0])
				else:
					full_list.append(temp[0])
					temp = []
					temp.append(animals)
					if zoo_animals[-1] == animals:
						full_list.append(temp[0])
		else:
			temp.append(animals)

	for index,animal in enumerate(full_list):
		animals_dict.update({index + 1: animal})
	print(animals_dict)	
	return animals_dict		

animals_dict = sort_animal()

def get_pen():
	animals_in_pen_list = []
	for pens in animals_dict:
		animals_in_pen_list.append(animals_dict[pens])
	print(animals_in_pen_list)

get_pen()				





