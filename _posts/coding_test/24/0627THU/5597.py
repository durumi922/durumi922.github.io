# abt=[1,2,3,4,5,6,7,8,9,10,
#      11,12,13,14,15,16,17,18,19,20,
#      21,22,23,24,25,26,27,28,29,30]

std=[i for i in range(1,31)]

for i in range(1,29):
    n = int(input())
    std.remove(n)

for i in std:
    print(i)

#print(std[i]) 하면 안되고
#print(i)해야함 ;;