'''
n = int(input())
v_list = []

for i in range(n):
    a = map(int,input().split())
    v_list.append(a)

v = int(input())

count = v_list.count(v)

print(count)
'''
'''
n = int(input())
v_list = []

a = map(int,input().split())
v = int(input())
v_list.append(a)

countV = v_list.count(v)
print(countV)
'''

n=int(input())
a = list(map(int, input().split()))
v= int(input())
count=0

for i in range(n):
    if a[i] == v:
        count += 1

print(count)

'''
뭐랄까 게시판 보고 풀었다.
1. 그냥 a = map(int, input().split())을
for문안에 넣으면 한 줄에 n개가 아니라 n줄을 입력해야함
2. 그냥 a == v 를하면 1 2 3 = 2 인거라서
리스트 안에 있는걸 대조해보고자 했으나 잘 몰랐다.
a[i] == v이걸 하면 i가 0 1 2 3이 될 때
a 안에 있는 인덱스 값에 따라서 하나하나 대조해보는것 이욜개꿀


'''





'''

특정문자열을 검색하기
str.count() 메서드 사용

text = "Hello, world!"
char = "o"

count = text.count(char)

if count > 0:
    print(f"'{char}'가 문자열에 포함되어 있습니다. 등장 횟수: {count}")
else:
    print(f"'{char}'가 문자열에 포함되어 있지 않습니다.")


'''