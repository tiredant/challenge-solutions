from sys import argv

script, filename = argv


def fizzbuzzer(x):
    current = open(x, 'r')

    for each in current:
        unit = each.split()
        for i in range (1,(int(unit[2])+1)):
            if i % int(unit[0]) == 0 and i % int(unit[1]) == 0:
                print "fb",
            elif i % int(unit[0]) == 0:
                print "f",
            elif i % int(unit[1]) == 0:
                print "b",
            else:
                print i,



fizzbuzzer(filename)
