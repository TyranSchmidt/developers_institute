# 3 <= 3 < 9
# 3 == 3 == 3
# bool(0)
# bool(5 == "5")
# bool(4 == 4) == bool("4" == "4")
# bool(bool(None))

# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)

a = int(input("give me a big number.")) 
b = int(input("give me a smaller number."))
if a > b:
	print("Hello World")


month = int(input("give me the number of a month 1-12:"))

if month > 2 and month < 6:
	print("Spring")
elif month > 5 and month < 9:
	print("Summer")
elif month > 8 and month < 12:
	print("Autumn")
elif month == 1 or month == 2 or month == 12:
	print("December")
else:
	print("That is not a valid entry.")