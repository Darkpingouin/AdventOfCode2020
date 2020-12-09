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
    total = 1
    for line in mylist:
        ll = re.split('bags contain|,',line)
        if (color_check in ll[0]):
            x = 0
            for i in range(1, len(ll)):
                if (ll[i].split()[0] != "no"):
                    nb = ll[i].split()[0]
                    color = ll[i].replace(nb, "").replace("bags", "").replace("bag", "").replace(".", "").strip()
                    total += int(nb) * get_nb_bags(mylist, color)
                    check_bags(mylist, color)
    print(total)
    return total
    

    return total
def main():
    mylist = sys.stdin.read().split("\n")
    bags_to_check = []
    total = 1
    check_bags(mylist, 'shiny gold')
    print(total)

if __name__ == "__main__":
    main()
