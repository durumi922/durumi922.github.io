listN=[]
for i in range(9):
    n=int(input())
    listN.append(n)

maxN = max(listN)

for i in range(9):
    if listN[i] == maxN:
        indexN = i+1
print(maxN)
print(indexN)

