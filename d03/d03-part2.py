import sys

def slide(right, down, mylist):
    index = 0
    linenb = 0
    tree = 0
    for line in mylist:
        line = line.rstrip()
        if (linenb % down == 0):
            if (line[index%len(line)] == '#'):
                tree += 1
            index += right
        linenb += 1
    return(tree)

def main():
    result = 1
    mylist = []
    for line in sys.stdin:
       mylist.append(line) 
    result *= slide(1,1,mylist)
    result *= slide(3,1,mylist)
    result *= slide(5,1,mylist)
    result *= slide(7,1,mylist)
    result *= slide(1,2,mylist)
    print(result)


if __name__ == "__main__":
    main()
