n,m = map(int,input().split())
b = []

#바구니에 1번부터 N번까지
for i in range(1, n+1):
    b.append(i)

#바구니 공 바꾸기
for _ in range(1, m+1):
    i,j = map(int,input().split())
    b[i-1], b[j-1] = b[j-1], b[i-1]     #지티피한테 물어본 리스트 스위치                 

for i in b:
    print(i, end=' ')
