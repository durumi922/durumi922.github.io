#내가 한것

ID_user = ["joon"]
ID = input("아이디를 입력하세요")

if (ID == ID_user):
    print("{ID}??!")
else:
    ID_user.append(ID)


#지티피를 통해 수정한것
ID_user = ["joonas","baekjoon"]
ID = input("아이디를 입력하세요")

if ID in ID_user:
    print(f"{ID}??!")
else:
    ID_user.append(ID)

#질문게시판을 보고 수정한것

ID_user = []
ID = input()
ID_user.append(ID)

if ID in ID_user:
    print(f"{ID}??!")

'''
이게 일단 쓸데없는 지시문을 넣어서는 안되고
모든 아이디로 전부 할 수 있어야했음
그래서 리스트 안에를 비우고, 인풋 구문 없애고, else 없애고
인풋하면 바로 append로 리스트에 들어가게 수정
'''