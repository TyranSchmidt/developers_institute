string = input("Give me a string that contains only 10 characters:")
length = len(string)
words = ""
if length == 10:
	print("The first character is " + string[0] + " and the last character is " + string[-1])
	for letters in string:
		words += letters
		print(words)
a = string[0] 
b = string[1] 
c = string[2] 
d = string[3] 
e = string[4] 
f = string[5] 
g = string[6] 
h = string[7] 
i = string[8] 
j = string[9] 
print(c + a + d + g + j + i + b + f + h + e)