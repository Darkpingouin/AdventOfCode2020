import sys
import re

def get_nb_bags(mylist, color_check):
    for line in mylist:
        ll = re.split('bags contain|,',line)
        result = 0
        for line in ll:
            if (ll[0] == color_check):
                nb = ll[i].split()[0]
                if (ll[i].split()[0] != "no"):
                    result += int(nb)
                else:
                    result += 1
    return result

def check_bags(mylist, color_check):
    print("checking " + color_check)
    for line in mylist:
        ll = re.split('bags contain|,',line)
        if (color_check in ll[0]):
            x = 1
            for i in range(1, len(ll)):
                if (ll[i].split()[0] != "no"):
                    nb = ll[i].split()[0]
                    color = ll[i].replace(nb, "").replace("bags", "").replace("bag", "").replace(".", "").strip()
                    x += int(nb) * check_bags(mylist, color)
                else:
                    return 1
            return x
    return 0
    
    
def main():
    mylist = sys.stdin.read().split("\n")
    bags_to_check = []
    total = check_bags(mylist, 'shiny gold') - 1
    print(total)

if __name__ == "__main__":
    main()
