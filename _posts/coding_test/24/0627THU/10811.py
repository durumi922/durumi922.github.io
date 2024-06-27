n,m = map(int,input().split())
b = []

#바구니에 1번부터 N번까지 번호 매기기
for idx in range(1, n+1):
    b.append(idx)


#바구니 공 바꾸기
for _ in range(1, m+1):
    i,j = map(int,input().split())
    b[i-1:j] = b[i-1:j][::-1]


for idx in b:
    print(idx, end=' ')

'''

b[i-1:j] = sorted(b[i-1:j], reverse=True)


5 4
(1 2)
2 1 3 4 5 (3 4)
2 1 4 3 5 (1 4)
4 3 2 1 5

(1 4)부분에서 자꾸 이상하게 뒤집힌 것을 확인
알고 보니까 sort가 순서대로 역순이라서 문제는 그냥 그 자체로 역순
순서대로 만든거라서 이상했던것,,





추가로

# b = list(range(1, n+1))
# 완전 간단하네


'''
