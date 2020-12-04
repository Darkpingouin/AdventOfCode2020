import sys

def check_line(myStr):
    mandatory = ['byr:','iyr:','eyr:','hgt:','hcl:', 'ecl:','pid:']
    attributes = myStr.split()
    nb = 0
    for item in mandatory:
        if any(item in s for s in attributes):
            nb+=1
    #print(attributes)
    #print(nb)
    return nb == 7

def valid_passport(mylist):
    nbValidPassports = 0
    nbAttributes = 0
    myStr = ""
    for line in mylist:
        line = line.rstrip()
        if line != "":
            myStr += line
        else:
            if (check_line(myStr)):
                nbValidPassports += 1
            myStr = ""
    if (check_line(myStr)):
                nbValidPassports += 1
    print(nbValidPassports)

def main():
    result = 1
    mylist = []
    for line in sys.stdin:
       mylist.append(line) 
    valid_passport(mylist)

if __name__ == "__main__":
    main()
