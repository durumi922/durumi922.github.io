n,x = map(int, input().split())
a = list(map(int, input().split()))
a_list=[]

for i in range(n):
    if a[i] < x:
        a_list.append(a[i])

for i in a_list:
    print(i, end=' ')


'''
거의 뭐 지티피가 다함
게시판도 보고
확실히 난이도가 올라가는데
근데 아직도 브론즈임 ;;

1. a_list.append(a[i]) 으로 리스트 전체가 아닌 특정 인덱스값만 넣기
2. for i in a_list: 리스트 값 출력
3. print(i, end=' ') 한줄로 공백 있게 출력

'''