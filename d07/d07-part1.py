import sys
import string
import re
def check_bags(bags, line, colorcheck):
    valid = []
    for i in range(1, len(bags)):
        if(colorcheck in bags[i]):
            valid.append(bags[0])
    return valid;

def main():
    result = []
    mylist = sys.stdin.read().split("\n")
    for line in mylist:
        bags = re.split("bags contain |,", line)
        bags = check_bags(bags, line, 'shiny gold')
        if (bags != []):
            result.append(bags)
    for bag in result:
        for line in mylist:
            bags = re.split("bags contain |,", line)
            bags = check_bags(bags, line, bag[0])
            if (bags != [] and bags not in result):
                result.append(bags)
    print(len(result))
if __name__ == "__main__":
    main()
