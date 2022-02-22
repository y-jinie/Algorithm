word = input()

#펠린드롬인가요?
if word == word[::-1]:
    print(1)
else:
    print(0)

#print(1 if word == word[::-1] else 0)
#print(int(word == word[::-1]))