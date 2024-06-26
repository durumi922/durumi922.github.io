import sys

t=int(sys.stdin.readline().rstrip())

for i in range(t):
    a,b =map(int,sys.stdin.readline().rstrip().split())
    print(a+b)


'''
문제에 적혀있는데 귀찮아서였는지 뭔가 흐린눈 이였는지
조건을 잘 못봤다


Python을 사용하고 있다면, input 대신 
sys.stdin.readline을 사용할 수 있다. 
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 
때문에 문자열을 저장하고 싶을 경우 
.rstrip()을 추가로 해 주는 것이 좋다.

'''