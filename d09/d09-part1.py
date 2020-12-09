import sys

def check_valid(mylist, size, index):
    for i in range(index - size, index):
        for j in range(index - size - 1, index):
            if (int(mylist[i]) + int(mylist[j]) == int(mylist[index])):
                return True;
    return False;

def main():
    mylist = sys.stdin.read().split("\n")
    size = 25
    for i in range(size, len(mylist)):
        if not check_valid(mylist, size, i):
            print(mylist[i])
        
    

if __name__ == "__main__":
    main()
