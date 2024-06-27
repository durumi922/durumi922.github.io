
n=[]

for i in range(10):
    a = int(input())
    n.append(a%42)

unique_values = len(set(n))
print(unique_values)



'''
리스트 내용물에 서로 다른 값이 몇 개 있는지 세는법

방법 1: set을 이용하는 방법
set은 중복을 허용하지 않는 자료형이므로 
리스트를 set으로 변환하면 고유한 값들만 남습니다.
그런 다음, len 함수를 사용하여 고유한 값의 개수를 구할 수 있습니다.

unique_values = len(set(numbers))
print(unique_values)

'''