class PigLatin:
	file = input("Input the text from the file: ")
	file = file.split(" ")
	vowels = "aeiouy"
	counter = 0
	for x in file:
		if x[0] in vowels:
			x += "yay"
		else:
			for a in range (len(x)):
				if x[a] in vowels:
					x = x[a] + x[a+1:] + x[:a] + "ay"
					break
		file[counter] = x
		counter +=1

	for r in file:
		print(r, end=" ")

