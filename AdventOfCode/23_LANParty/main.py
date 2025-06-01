import re

connections = {}
f = open("data.txt")
for line in f:
    pairs = line.split('-')
    pairs[0] = pairs[0].strip()
    pairs[1] = pairs[1].strip()
    if pairs[0] in connections:
        connections[pairs[0]].append(pairs[1])
    else:
        connections[pairs[0]] = [pairs[1]]

    if pairs[1] in connections:
        connections[pairs[1]].append(pairs[0])
    else:
        connections[pairs[1]] = [pairs[0]]

print(connections)

# Part 1
# connection_trios = []
# for key, source in connections.items():
#     if len(source) >= 2:
#         i = 0
#         for ii in range(i, len(source)):
#             second = source[ii]
#             for iii in range(ii, len(source)):
#                 third = source[iii]
#                 if third in connections[second]:
#                     there = False
#                     for trio in connection_trios:
#                         if key in trio and second in trio and third in trio:
#                             there = True
#                     if not there:
#                         connection_trios.append([key, second, third])
#             i += 1

# count = 0
# for trio in connection_trios:
#     if re.search('^t', trio[0]) or re.search('^t', trio[1]) or re.search('^t', trio[2]):
#         count += 1

# print(connection_trios)
# print(count)

# Part 2
largest_connective = []
connective = []
for key, source in connections.items():
    if len(source) > len(largest_connective):
        i = 0
        for ii in range(i, len(source)):
            second = source[ii]
            for iii in range(ii, len(source)):
                third = source[iii]
