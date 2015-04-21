from sys import argv
script, filename = argv

item = open(filename,"r")

for each in item:
	number = ' '.join(each)
	box =[]
	for each in number:
		if each.isdigit() == True:
			box.append(int(each))
	print sum(box)
		
		
		
