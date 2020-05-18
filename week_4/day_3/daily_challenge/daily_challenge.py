user_input = input("Do you want to encrypt or decrypt (text-sensitive)?: ")
user_text = input("Please enter the text: ")
enc_text = ""
dec_text = ""
for i in range(len(user_text)):
	character = user_text[i]
	if user_input == "encrypt": 
		enc_text += chr(ord(character) + 3)		
	elif user_input == "decrypt":
		dec_text += chr(ord(character) - 3)		
	else:
		print("That is not a valid argument.")

if user_input == "encrypt":
	print(enc_text)
elif user_input == "decrypt":
	print(dec_text)

