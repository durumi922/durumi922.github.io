while True:
    try:
        a,b = map(int,input().split())
        print (a+b)
    except:
        break

"""
뭔가 이상하긴 했음 근데 일단 틀려주고나서 게시판을 봤음
그랬더니 뭔가 마무리를 할 수 있어야함
아무튼 트라이 익셉트문을 사용해야함

와일문으로 무한 반복하기
트라이문으로 탈출하기

EOF에 대해 배우는 문제
"""