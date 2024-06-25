a = int(input())
b = int(input())

if 0 < a <= 1000 and 0 < b <= 1000:
    print("1")
elif -1000 <= a <0 and 0 < b <= 1000:
    print("2")
elif -1000 <= a <0 and -1000 <= b <0:
    print("3")
elif 0 < a <= 1000 and -1000 <= b <0:
    print("4")