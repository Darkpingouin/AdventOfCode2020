import sys 

def check_loop(mylist):
    indexes = []
    index = 0
    acc = 0
    while(True):
        i = mylist[index].split()
        indexes.append(index)
        if (i[0] == "acc"):
            acc += int(i[1])
            index += 1
        elif(i[0] == "jmp"):
            index += int(i[1])
        elif(i[0] == "nop"):
            index += 1
        if (index in indexes):
            return False
            break;
        elif (index == len(mylist)):
            print(acc)
            return True;
            break;

def main():
    mylist = sys.stdin.read().split("\n")
    for i in range(len(mylist)):
        c = mylist.copy()
        if ("nop" in c[i]):
            c[i] = c[i].replace("nop", "jmp")
            if check_loop(c):
                break;
        if ("jmp" in c[i]):
            c[i] = c[i].replace("jmp", "nop")
            if check_loop(c):
                break;


if __name__ == "__main__":
    main()
