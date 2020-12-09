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
    mylist = list(map(int, mylist))
    for i in range(index):
        curr_sum = mylist[i]
        j = i + 1 
        while j <= index:
            if curr_sum == number:
                print(min(mylist[i:j]) + max(mylist[i:j]))
                return 1
            if curr_sum > number or j == index:
                break
            curr_sum = curr_sum + mylist[j]
            j += 1
    return 0
    

def main():
    mylist = sys.stdin.read().split("\n")
    size = 25
    for i in range(size, len(mylist)):
        if not check_valid(mylist, size, i):
            number = int(mylist[i])
            print(number)
            break;
    find_sum(mylist, number, i)
