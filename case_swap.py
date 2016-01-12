import sys

with open(sys.argv[1],"r") as f:
    for each in f:
        bench = []
        for each in each:
            if each.isalpha() == True:
                if each.isupper() == True:
                    bench.append(each.lower())
                else:
                    bench.append(each.upper())
            elif each != "\n":
                bench.append(each)
        print "".join(bench)
