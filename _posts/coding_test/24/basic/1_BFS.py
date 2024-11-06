"""
1. 아이디어
- 2중 for => 값 1 && 방문 x => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 >> 가능!

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문 : bool[][]
- Queue(BFS)

"""

import sys
input = sys.stdin.readline
#입출력문을 빠르게 해주는 코드

n,m = map(int, input().split())
map = [list(map(int,input.split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
#기본적인 자료구조 준비

dy = [0,1,0,-1]
dx = [1,0,-1,0]
#이거 이동하는거임 외워두기

def bfs(y,x):
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] =True
                    q.append((ny,nx))
    return rs

cnt = 0
maxy = 0
#최대값
#변수 설정

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            #값이 1이면서 방문하지 않았다면

            #다시 방문하지 않음
            chk[j][i] = True

            #전체 그림 갯수들 +1
            cnt += 1 

            # BFS > 그림 크기를 구하고
            maxy = max(maxy, bfs(j,i))
            # 최대값 갱신
            
#이중 포문
            
