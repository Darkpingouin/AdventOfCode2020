import sys

def calc_direction(current_direction, d, instruction):
    directions = ['N', 'E', 'S', 'O']
    index = directions.index(current_direction)
    if (instruction == 'L'):
        if (index - d >= 0):
            return directions[index - d]
        else:
            return directions[len(directions) - index - d]
    elif (instruction == 'R'):
        if (index + d < len(directions)):
            return directions[index + d]
        else:
            return directions[index + d - len(directions)]

def calc_route(instructions):
    directions = ['N', 'E', 'S', 'O']
    current_direction = 'E'
    x = 0 
    y = 0
    for i in instructions:
        if i[0] == 'R' or i[0] == 'L':
            d = int(i.replace(i[0], '')) / 90
            current_direction = calc_direction(current_direction, int(d), i[0])
        if i[0] == 'F':
            i = i.replace('F', current_direction)
        if (i[0] == 'N'):
            n = int(i.replace('N', ''))
            y += n
        if (i[0] == 'S'):
            n = int(i.replace('S', ''))
            y -= n
        if (i[0] == 'E'):
            n = int(i.replace('E', ''))
            x += n
        if (i[0] == 'O'):
            n = int(i.replace('O', ''))
            x -= n
    print(abs(x) + abs(y))
def main():
    instructions = sys.stdin.read().split("\n")
    calc_route(instructions)
    
main()
