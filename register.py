import sys
import csv
from decimal import *
with open(sys.argv[1],"r") as f:
	reader = csv.reader(f,delimiter=';')
	for row in reader:
		unit = float(row[1])-float(row[0])
		
		
		bench = []
		if unit < 0.00:
			bench.append("ERROR")
		if unit == 0.00:
			bench.append("ZERO")
		def change(data):
			if data >= 100.00:
				data -= 100.00
				bench.append("ONE HUNDRED")
				change(data)
			elif 100.00 > data >= 50.00:
				data -= 50.00
				bench.append("FIFTY")
				change(data)
			elif 50.00 > data >= 20.00:
				data -= 20.00
				bench.append("TWENTY")
				change(data)
			elif 20.00 > data >= 10.00:
				data -= 10.00
				bench.append("TEN")
				change(data)
			elif 10.00 > data >= 5.00:
				data -= 5.00
				bench.append("FIVE")
				change(data)
                        elif 5.00 > data >= 2.00:
                                data -= 2.00
				bench.append("TWO")
				change(data)
			elif 2.00 > data >= 1.00:
				data -= 1.00
				bench.append("ONE")
				change(data)
			elif 1.00 > data >= .50:
				data -= .50
				bench.append("HALF DOLLAR")
				change(data)
			elif .50 > data >= .25:
				data -= .25
				bench.append("QUARTER")
				change(data)
			elif .25 > data >= .10:
				data -= .10
				bench.append("DIME")
				change(data)
			elif .10 > data >= .05:
				data -= .05
				bench.append("NICKEL")
				change(data)
				
			elif .05 > round(data,2) >= .01:
				data -= .01
				bench.append("PENNY")
				change(data)
			else:
				print ",".join(bench)
		change(unit)
		
