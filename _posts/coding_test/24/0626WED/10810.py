n,m = map(int,input().split())
b=[]

#바구니 만들기
for _ in range(n):
    b.append(0)

for _ in range(m):
    i,j,k = map(int,input().split())
    

#바구니에 범위에 따라서 공 넣기
for _ in range(m):
    for _ in range(i,j+1):
        b[i:j+1] = [k]


for i in b:
    print(i, end=' ')


#-----------------------------------------------

n,m = map(int,input().split())

# 바구니 초기화
# 이렇게도 하는 군 깔꼼한디?
b = [0] * n

for _ in range(m):
    i,j,k = map(int,input().split())
    

#바구니에 범위에 따라서 공 넣기
for _ in range(m):
    for idx in range(i-1,j):    #그렇구만.. 레인지 안에 범위 말고
        b[idx] = k            #idx 값으로 하는거구만,,
                                #[k]가 아니라 k 그렇군,,
#그리고 이거 따로 빼면 이게 입력값의 마지막 것만 들어가게됨


for i in b:
    print(i, end=' ')

#-------------------------------------------------

n,m = map(int,input().split())

# 바구니 초기화
b = [0] * n

#바구니에 범위에 따라서 공 넣기
for _ in range(m):
    i,j,k = map(int,input().split())
    for idx in range(i-1,j):  
        b[idx] = k        
                 

for i in b:
    print(i, end=' ')







