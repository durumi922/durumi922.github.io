t= int(input())

for i in range(t):
    r,s =input().split() 
    r = int(r) #반복 횟수를 정수로 변환
    p="" #t개의 테스트 케이스가 있는데 매번 초기화해줘야 누적 안됨
 
    for i in s: #S 문자열 i번째를 r번 반복해서 p에 추가
        p += i*r 
    
    print(p)


    