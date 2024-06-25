H,M = map(int, input().split())

if 0<H<=23 and 0<M<=59 :
    time45 = H*60 + M - 45
    H = time45 // 60 
    M = time45 % 60
    print(H , M)

elif H==0 and 0<M<=59 :
    H=24
    time45 = H*60 + M - 45
    H = time45 // 60 
    M = time45 % 60
    print(H , M)    


#0 45 인 경우 24 0 으로 출력됨 -> 0 0 으로 출력되어야함

H,M = map(int, input().split())

if 0<H<=23 and 0<M<=59 :
    time45 = H*60 + M - 45
    H = time45 // 60 
    M = time45 % 60
    print(H , M)

elif H==0 :
    H=24
    time45 = H*60 + M - 45
    H = time45 // 60 
    M = time45 % 60

    if H==24:
        H=0
        
    print(H , M)    

#또 통과가 안되길래 다시 게시판을 찾아보았고 
#반례를 테스트 해보라고 해서 테스트 해봄
#쭉 다 되는데 17 0이 안되는 것을 확인
#if 0<H<=23 and 0<M<=59 : 에서
#0<=M=59로 등호를 빼먹은 것을 확인
#어케 이제껏 통과 되었는지가 의문

H,M = map(int, input().split())

if 0<H<=23 and 0<=M<=59 : 
    time45 = H*60 + M - 45
    H = time45 // 60 
    M = time45 % 60
    print(H , M)

elif H==0 :
    H=24
    time45 = H*60 + M - 45
    H = time45 // 60 
    M = time45 % 60

    if H==24:
        H=0
        
    print(H , M)   