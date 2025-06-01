from collections import deque

f = open("data.txt")

rules = set()

line = f.readline()
line = line.strip()
while line != "":
    rules.add(tuple(map(int, line.split('|'))))
    line = f.readline()
    line = line.strip()

print(rules)

dq = deque()

number = f.readline(2)
dq.append(number)
f.readline(1)
number = f.readline(2)
while number != "":
    i = 0
    for nb in dq:
        for tp in rules:
            print(str(nb) + " == " + str(tp[0]) + " and " + str(number) + " == " + str(tp[1]))
            if str(nb) == str(tp[0]) and str(number) == str(tp[1]):
                dq.append(number)
                print("caca")
            elif nb == tp[1] and number == tp[0]:
                dq.appendleft(number)
    f.readline(1)
    number = f.readline(2)

print(dq)
