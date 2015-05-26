from sys import argv

script,filename =argv

current = open(filename,'r')

for each in current:
	bench = []
	
	if len(each)>7:
		try:
			
			fizz = each[0:2]
			bench.append(int(fizz))
			buzz = each[2:5]
			bench.append(int(buzz))
			how_high = each[5:10]
			bench.append(int(how_high))
			
			print \
			
		
		
			for i in range(1,int(bench[2])+1),:
				for z in i:
					if z%bench[0]==0 and z%bench[1]==0:
						print 'FB',
					elif z%bench[0]==0:
						print 'F',
					elif z%bench[1]==0:
						print 'B',
					elif z > int(bench[2]):
						print z,
					else:
						print z,
						
		except ValueError:
			bench = []
	
			fizz = each[0:1]
			bench.append(int(fizz))
			buzz = each[2:4]
			bench.append(int(buzz))
			how_high = each[4:10]
			bench.append(int(how_high))
			
