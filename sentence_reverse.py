from sys import argv

script, filename = argv

current = open(filename,"r")

for each in current:
    unit = each.split()
    done = unit[::-1]
    print " ".join(done)
