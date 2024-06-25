a,b,c = map(int,input().split())

#같은 눈이 3개 나온 경우
if a==b==c:
    money = 10000 + a * 1000

#같은 눈이 2개 나온 경우    
elif a==b or b==c :
    money = 1000 + b * 100

elif a==c:
    money = 1000 + a * 100

#모두 다른 눈이 나온 경우
elif a != b != c:

    #a가 가장 큼
    if a> b and a > c:
        money = a*100
    
    #b가 가장 큼
    elif b> a and b > c:
        money = b*100 

    #c가 가장 큼   
    elif c> a and c > a:
        money = c*100  

print(money)
