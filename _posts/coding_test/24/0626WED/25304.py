x=int(input())
n=int(input())
receipt = []

for i in range(1,n+1):               #물건값을 게산해서 리스트에 넣음
    a,b = map(int,input().split())
    receipt.append(a*b)

total =0
for i in receipt:                   #리스트 안에 있는 내용물 다 더함
    total += i

if x == total :                     #영수증값과 계산값을 비교
    print("Yes")
else:
    print("No")