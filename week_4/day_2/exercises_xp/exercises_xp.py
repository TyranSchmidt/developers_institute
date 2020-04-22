#exercise
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

basket.remove("Banana")
basket.pop(2)
basket.append("Kiwi")
basket.insert(0, "Apples")

Apples = 0
for i in basket:
	if i == "Apples":
		Apples += 1
print(f"There are {Apples} apples in the basket.")

basket = []
print(basket)


#exercise1
my_fav_numbers = {7, 13, 21}
my_fav_numbers.add(17)
my_fav_numbers.add(25)
my_fav_numbers.remove(25)
print(my_fav_numbers)

friend_fav_numbers = {16, 22, 49}
our_fav_numbers = my_fav_numbers
our_fav_numbers.update(friend_fav_numbers)
print(our_fav_numbers)


#exercise2
my_tuple_numbers = (3, 8, 11)
my_tuple_numbers = list(my_tuple_numbers)
my_tuple_numbers.append(16)
my_tuple_numbers.append(26)
my_tuple_numbers.pop(-1)

tuple_friend_numbers = (15, 1, 56)
tuple_friend_numbers = list(tuple_friend_numbers)
our_tuple_numbers = my_tuple_numbers
our_tuple_numbers += my_tuple_numbers
our_tuple_numbers = tuple(our_tuple_numbers)
print(our_tuple_numbers)

#exercise3
"A float is an integer with a decimal"
"yes"


list_float = []
n = 1.5 
o = 2
while o < 6:
	list_float.append(n)
	n += 1	
	list_float.append(o)
	o += 1
print(list_float)

#exercise4
quit = False
while quit == False:
	topping = input("Add a topping or type quit to stop:")
	if topping == "quit":
		quit = True
		print("That is all.")
	else:
		print(f"We will add {topping} to your pizza.")

#exercise5
age = float(input("Give me your age"))
if age <= 3 and age > 0:
	print("Entry is free")
elif age <= 12 and age > 3:
	print("The ticket is $10")
elif age > 12:
	print("The ticket is $15")
else:
	print("That's not a valid age")


#exercise6
new_list = [3, "hi", "eat", 71, "goodbye"]

list_num = 0
while list_num < len(new_list):
	print(new_list[list_num])
	list_num += 1

# exercise7

done = False
total_cost = 0
while done == False:
	new_age = input("Give me a member of your family's age or type 'done' when you are done:")
	if new_age == "done":
		done = True
		print(f"The total cost for your family is ${total_cost}, welcome.")
	else:	
		new_age = float(new_age)	
		if new_age <= 3 and new_age > 0:
			print("Entry is free")
		elif new_age <= 12 and new_age > 3:
			print("The ticket is $10")
			total_cost += 10
		elif new_age > 12:
			print("The ticket is $15")
			total_cost += 15
		else:
			print("That's not a valid age")


# exercise 8

exer_8_list = [3, "hi", "eat", 71, "goodbye"]

exer_8_len = len(exer_8_list)
exer_8_index = 0
while exer_8_index < exer_8_len:
	if exer_8_index % 2 == 0:
		print(exer_8_list[exer_8_index])
	exer_8_index += 1

# exercise 9

done = False
teen_list = []
while done == False:
	teen_age = input("Give me a member of your group's age or type 'done' when you are done:")
	if teen_age == "done":
		done = True
		if len(teen_list) == 0:
			print("None of you may enter")
		elif len(teen_list) == 1:
			print("Only you may enter")
		else:
			print("you", len(teen_list) , "may enter")
	else:	
		teen_age = float(teen_age)	
		if teen_age <= 21 and teen_age >= 16:
			print("You may not enter")
		elif teen_age < 16 and teen_age > 0 or teen_age > 21 and teen_age < 100:
			print("You may enter")
			teen_list.append("entree")
		else:
			print("That's not a valid age")


# exercise 10

user_list = ["John", "Luke", "Mary", "Lisa", "Robert"]

user_num = 0
while user_num < len(user_list):
	user_name = user_list[user_num]
	user_age = int(input(f"{user_name} how old are you?"))
	if user_age < 16:	
		user_list.remove(user_name)
	else:	
		user_num += 1
print(user_list)

