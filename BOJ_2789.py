#LOVA를 만들어주기 위해
word = input()

#immutable
for i in "CAMBRIDGE":
    word = word.replace(i, "")

print(word)