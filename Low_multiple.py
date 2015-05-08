from sys import argv

script,filename = argv

current = open(filename,'r')

for each in current:
	x = int(each[0]+each[1])
	n = int(each[3]+each[4])
	
	def task():
		counter = 0
	
		while counter <= x:
			
			
			ticker = 1
			counter += (n * ticker)
			ticker += 1
			
		
			if counter >=x:
				print counter
				
				
				break
	task()
