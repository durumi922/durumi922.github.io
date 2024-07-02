

alphaPlaces = {}
word = input()
index = 0
for c in word:
    if ord(c) not in alphaPlaces:
        alphaPlaces[ord(c)] = index

    index += 1

for i in range(97, 123):
    print(-1 if i not in alphaPlaces else alphaPlaces[i], end=" ")