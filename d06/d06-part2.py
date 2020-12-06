import sys
import string

def check_group(sublist):
    nbpeople = len(sublist.split())
    questions = string.ascii_lowercase
    answers = 0
    for letter in questions:
        if (sublist.count(letter) == nbpeople):
            answers += 1
    return(answers)


def main():
    mylist = sys.stdin.read().split("\n\n")
    result = 0
    for sublist in mylist:
        result += check_group(sublist)
    print(result)

if __name__ == "__main__":
    main()
