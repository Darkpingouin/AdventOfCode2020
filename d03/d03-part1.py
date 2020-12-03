import sys
index = 0
tree = 0
for line in sys.stdin:
    line = line.rstrip()
    while (index >= len(line)):
        line += line
    if (line[index] == '#'):
        lines = list(line)
        lines[index] = 'X'
        line = "".join(lines)
        tree += 1
    else:
        lines = list(line)
        lines[index] = '0'
        line = "".join(lines)
    print(line)
    index += 3
print(tree)
