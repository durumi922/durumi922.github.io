sub = int(input())
score = list(map(int,input().split()))

m= max(score)
a=[]

for i in score:
    a.append(i/m*100)

total = 0 

for i in a:
    total += i

print(total/sub)

'''
하,,, 스스로의 힘으로 풀어서
너무나 보람상조,,, 뿌듯,,,,
내 실력이 늘었다....

중요한점은 리스트 안에 있는걸 하나씩 꺼내고 사용하고 싶다면

for i in score:
    a.append(i/m*100)

이거처럼 in 리스트명 하고
안에 하나씩 꺼내는건 i로 하면 됨.... 기깔나다..

'''