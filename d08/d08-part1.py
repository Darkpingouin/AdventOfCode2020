import sys 

def main():
    mylist = sys.stdin.read().split("\n")
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
            break;
        
    print(acc)

if __name__ == "__main__":
    main()
