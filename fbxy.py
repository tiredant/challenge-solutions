from sys import argv

script,filename =argv

current = open(filename,'r')

for each in current:
    print len(each)
    bench = []
    if len(each)>7:
        fizz = ("".join(each[0:2]))
        bench.append(fizz)
        buzz = each[2:5]
        bench.append(buzz)
        how_high = each[5:10]
        bench.append(how_high)
        for i in range(1,int(bench[2])),:
            paper = []
            paper.append(i)
        print "".join(str(paper))
