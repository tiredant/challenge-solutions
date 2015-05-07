from sys import argv
script,filename = argv
current = open(filename,'r')
counter = 0
for each in current:
    counter += int(each)
print counter
