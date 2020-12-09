import sys

def check_valid(mylist, size, index):
    for i in range(index - size, index):
        for j in range(index - size - 1, index):
            if (int(mylist[i]) + int(mylist[j]) == int(mylist[index])):
                return True;
    return False;

def total_list(mylist):
    total = 0
    for nb in mylist:
        total += int(nb)
    return total

def find_sum(mylist, number, index):
    for i in range(index):
        for j in range(1, index):
            if (total_list(mylist[i:j]) == number):
                return(int(min(mylist[i:j])) + int(max(mylist[i:j])))

def main():
    mylist = sys.stdin.read().split("\n")
    size = 25
    for i in range(size, len(mylist)):
        if not check_valid(mylist, size, i):
            number = int(mylist[i])
            break;
    print(find_sum(mylist, number, i))
        
    

if __name__ == "__main__":
    main()
