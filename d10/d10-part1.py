import sys

def check_list(mylist):
    three = 0
    one = 0
    comp = 0
    for nb in mylist:
        if (nb - comp == 1):
            one += 1
        elif (nb - comp == 3):
            three += 1
        comp = nb
    three += 1
    print(one * three)

def main():
    mylist = sys.stdin.read().split("\n")
    mylist = list(map(int, mylist))
    mylist.sort()
    check_list(mylist)
    print(mylist)
