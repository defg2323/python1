
line = int(input("Diamond의 길이를 입력 : "))

for x in range(1, line * 2, 2):
    print((" " * ( (line * 2 - 1 -x)//2))+("*" * x))

for i in range(line * 2 -3, 0, -2):
    print((" " * ( (line * 2 - 1 -i)//2)) + "*"*i)