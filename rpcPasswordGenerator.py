import random

passwords = []

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
punctuation = """'!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'"""

string = [lowerCase,upperCase,digit,punctuation]

def getLength():
	length = random.randrange(8, 32)
	tab = [string[random.randrange(0,4)] for x in range(length)]

	if lowerCase in tab and upperCase in tab and digit in tab and punctuation in tab:
		return tab
	return False

while 1:
	length = getLength()
	if length != False:
		for chars in length:
			char = chars[random.randrange(0, len(chars))]
			if passwords.count(char) < 2:
				passwords.append(char)
			else:
				length.append(chars)
		break

print(''.join(passwords))
