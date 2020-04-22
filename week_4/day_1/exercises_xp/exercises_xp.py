print("Hello world\n" * 4)

print((99^3) * 8)

name = "Tyran"
age = 21
shoe_size = 7
info = f"My name is {name}, I am {age} years old and have a shoe size of {shoe_size}."
print(info)

computer_brand = "MSI"
print(f"I have a {computer_brand} computer.")

# 5 < 3
# 3 == 3
# 3 == "3"
# "3" > 3
# "Hello" == "hello"

height = int(input("Give me your height in inches"))

if height < 35:
	print("Sorry you are not tall enough to ride this rollercoaster.")
else:
	print("Welcome aboard the rollercoaster.")

given_number = int(input("Give me a number."))

if given_number % 2 == 0:
	print("You gave me an even number.")
else:
	print("You gave me an odd number.")
