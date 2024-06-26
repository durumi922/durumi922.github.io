t=int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    print(a+b)
    # i+=i

# for i in range(1,t+1):
#     print(a+b)
#     # i+=i

#사실 끊어서 출력되어도 상관없는데 한번에 주르륵 출력하고 싶다면
#리스트에 넣어서 하기!! 와우!

T = int(input())
answers = []

for _ in range(T):
    A, B = map(int, input().split())
    answers.append(A + B)
    
for i in range(T):
    print(answers[i])

'''
여기서 _과 i의 차이
_는 반복할 때 변수 안씀
i는 반복할 때 변수 씀

반복 실행
반복 실행
반복 실행
반복 실행
반복 실행


현재 반복 횟수: 0
현재 반복 횟수: 1
현재 반복 횟수: 2
현재 반복 횟수: 3
현재 반복 횟수: 4

다음과 같이 반복 횟수를 드러내고 싶으면 i써야함

'''