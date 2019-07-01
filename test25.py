list1 = []
list2 = []
value = 3

for i in range(0,5):
    for k in range(0,4):
        list1.append(value)
        value +=3
    list2.append(list1)
    list1 = []
print(list2)
for i in range(0,5):
    for k in range(0,4):
        print("%3d" % list2[i][k], end=" ")
    print()
