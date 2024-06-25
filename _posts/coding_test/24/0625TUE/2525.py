# A, B = map(int, input().split())
# C = int(input())

# if 0<A<=23 and 0<=B<=59 : 
#     timeC = A*60 + B + C
#     A = timeC // 60 
#     B = timeC % 60
#     print(A , B)

# elif A==0 :
#     A=24
#     timeC = A*60 + B + C
#     A = timeC // 60 
#     B = timeC % 60
#     if A==24:
#         A=0
        
#     print(A , B)   


#근데 C가 1000까지 가능함

A, B = map(int, input().split())
C = int(input())

if 0<A<=23 and 0<=B<=59 : 

    timeC = A*60 + B + C

    if timeC >= 1440:
        timeC-1440
    
    elif timeC >= 2880:
        timeC-1440    

    A = timeC // 60 
    B = timeC % 60

    if A==24:              
        A=0    
   
    print(A , B) 

elif A==0 :
    A=24
    timeC = A*60 + B + C

    if timeC >= 1440:
        timeC-1440
    
    elif timeC >= 2880:
        timeC-1440 

    A = timeC // 60 
    B = timeC % 60

    if A==24:              
        A=0    
   
    print(A , B) 

#23 48
#1000
#하면 40 28 나옴 무조건 24 이내로 해야함
#뭔가 빼다가 A에서 24를 빼다가 24 완전될때까지 또 빼야겠다 싶었다가
#그냥 와일문으로 반복하는게 나을 듯 싶어서
#지티피한테 와일문 만들어달라고 함(문법 몰라서)
#그러고 완벽 작동
#근데 그 전까지 왜 작동이 안됐었는지는 모르겠음
#지금은 날려버렸지만 A에서 24 빼는거 했는데도 그대로 40으로 남았음

A, B = map(int, input().split())
C = int(input())

if 0<A<=23 and 0<=B<=59 : 

    timeC = A*60 + B + C 

    A = timeC // 60 
    B = timeC % 60

    while A>= 24:
        A -= 24

    print(A , B) 

elif A==0 :
    A=24
    timeC = A*60 + B + C

    A = timeC // 60 
    B = timeC % 60

    while A>= 24:
        A -= 24
        
    if A==24:              
        A=0    
   
    print(A , B) 
