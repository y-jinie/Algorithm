n = int(input())
line = "* " * n

#slicing
for i in range(n):
    print(line)
    line = line[::-1]