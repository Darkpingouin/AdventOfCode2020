import sys

def check_row(mylist):
    maxID = 0
    ids = []
    for line in mylist:
        line = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        row = int(line[0:7],2)
        col = int(line[7:10],2)
        id = row * 8 + col
        ids.append(id)

    for i in range(min(ids), max(ids)):
        if (i not in ids):
            print(i)

def main():
    mylist = []
    for line in sys.stdin:
       mylist.append(line)
    check_row(mylist)


if __name__ == "__main__":
    main()
