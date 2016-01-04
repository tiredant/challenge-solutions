import sys
import csv

def flavor(death_list,knife):
	bench = []
	counter = 0
	while len(death_list)> 0:
		for each in death_list:
			counter += 1
			if counter is int(knife):
				bench.append(str(each))
				death_list.pop(death_list.index(each))
				counter = 1
	print " ".join(bench)
with open(sys.argv[1],'r') as f:
	reader = csv.reader(f,delimiter = ",")
	for each in reader:
		l = list(xrange(int(each[0])))
		flavor(l,each[1])
