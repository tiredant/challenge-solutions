import sys

def hex_con(x):
    i = int(x,16)
    print i

with open(sys.argv[1],"r") as f:
    for each in f:
        hex_con(each)
