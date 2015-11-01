def multitable():
    for each in range(1, 13):
        for i in range(1, 13):
            print "{:4d}".format(each * i),
        print
multitable()
