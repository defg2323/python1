list1 = []
list2 = []
list3 = []
value =0
result= ""
for i in range(0,5):
    for k in range(0,4):
        value +=3
        for l in range(1,10):
            result = str("%2dX  %2d = %2d" % (value, l, value*l))
            list1.append(result)
        list2.append(list1)
        list1 = []
    list3.append(list2)
    list2 = []
print(list3)
print(len(list3))
for i in range(0,5):
    for k in range(0,4):
        for l in range(0,9):
           aa = aa + ("%s" % list3[i][k][l])
    print()
print(aa)
