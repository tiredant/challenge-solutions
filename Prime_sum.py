def sieve():
	composite = []
	prime=[]
	x = 10000
	
	for each in xrange(2,x+1):
		if each not in composite:
			prime.append(each)
			if len(prime)> 999:
				print len(prime)
				print sum(prime)
				break
		for i in xrange(each*each,x+1,each):
				composite.append(i)		
		
sieve()
