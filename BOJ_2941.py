#크로아티아 알파벳
#1. replace 이용
word = input()
changes = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for change in changes:
    word = word.replace(change, ".")

print(len(word))

#2. count 이용
word = input()
changes = ['=', "-", "lj", "nj", "dz="]
total = len(word)

for change in changes:
    total -= word.count(change)
print(total)