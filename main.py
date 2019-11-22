import itertools
import datetime
import os

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOLS = r",<.>/?;:'[{}]\|!@#$%^&*()_-+=`~" + '"'
DIGITS = "1234567890"

help_message = \
r"""
                                    ++ Wordlist Generator ++

 [+] Please select which characters to include in your character set...

            [0] All characters
            [1] Lowercase alphabetical characters
            [2] Uppercase alphabetical characters
            [3] Symbols
            [4] Digits
"""
def main():
	character_set = []
	filename = "wordlist"+str(datetime.datetime.today())
	filename = filename.replace(" ","")
	filename = filename.replace(":","")
	filename = filename.replace(".","")
	filename+=".txt"
	total_chatacters = 0

	print(help_message)
	choice = input("<user> ")

	if "0" in choice:
		for character in LOWERCASE:
			character_set.append(character)
		for character in UPPERCASE:
			character_set.append(character)
		for character in SYMBOLS:
			character_set.append(character)
		for character in DIGITS:
			character_set.append(character)

	if "1" in choice:
		for character in LOWERCASE:
			character_set.append(character)

	if "2" in choice:
		for character in UPPERCASE:
			character_set.append(character)

	if "3" in choice:
		for character in SYMBOLS:
			character_set.append(character)

	if "4" in choice:
		for character in DIGITS:
			character_set.append(character)

	elif "0" not in choice and "1" not in choice and "2" not in choice and "3" not in choice and "4" not in choice:
		print("[!] Invalid choice. Do you want to run again? (Y or N) ")
		response = input("<user> ")
		if response.lower() == "y":
			try:
				os.system("cls")
			except:
				os.system("clear")
			main()
		else:
			return

	print("[+] Please enter the minimum word length...")
	lower_limit = input("<user> ")
	print("[+] Please enter the maximum word length...")
	upper_limit = input("<user> ")
	file_write = open(filename,"w")

	for length in range(int(lower_limit),int(upper_limit)+1):
		combinations = itertools.product(character_set,repeat=length)
		for each in combinations:
			combination = ""
			combination = combination.join(each)
			file_write.write(combination+"\n")
		total_chatacters+=len(character_set)**length
		print("[+] Completed all combinations os length",length)

	file_write.close()
	print("\n[*] Done. File saved as",filename)
	print("\n[+] Do you want to run again? (Y or N) ")
	response = input("<user> ")
	if response.lower() == "y":
		try:
			os.system("cls")
		except:
			os.system("clear")
		main()
	else:
		return

main()
