import sys
def romans(x):


    marker = 0
    bench = []
    while marker < int(x):
        difference = int(x) - marker
        if difference >= 1000:
            marker += 1000
            bench.append("M")
        elif 1000 > difference >= 900:
            marker += 900
            bench.append("CM")
        elif 900 > difference >= 500:
            marker += 500
            bench.append("D")
        elif 500 > difference >= 100:
            marker += 100
            bench.append("C")
        elif 100 > difference >= 90:
            marker += 90
            bench.append("XC")
        elif 90 > difference >= 50:
            marker += 50
            bench.append("L")
        elif 50 > difference >= 40:
            marker += 40
            bench.append("XL")
        elif 40 > difference >= 10:
            marker += 10
            bench.append("X")
        elif 10 > difference >= 9:
            marker += 9
            bench.append("IX")
        elif 9 > difference >= 5:
            marker += 5
            bench.append("V")
        elif 5 > difference >= 4:
            marker += 4
            bench.append("IV")
        elif 4 > difference >= 1:
            marker += 1
            bench.append("I")
        else:
            pass

    print "".join(bench)

with open(sys.argv[1], "r") as f:
    for each in f:
        romans(each)
