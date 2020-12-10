import sys 

def tribonnacci(n):
    if (n <= 0):
        return 1
    elif (n == 1):
        return 1
    elif (n == 2):
        return 2 
    else:
        return tribonnacci(n-1) + tribonnacci(n-2) + tribonnacci(n-3)

def check_list(mylist):
    one = 0
    comp = 0
    total = 1
    for nb in mylist:
        if (nb - comp == 1):
            one += 1
        elif (nb - comp == 3):
            total *= tribonnacci(one)
            one = 0
        comp = nb
    total *= tribonnacci(one)
    print(total)

def main():
    mylist = sys.stdin.read().split("\n")
    mylist = list(map(int, mylist))
    mylist.sort()
    check_list(mylist)

main()
