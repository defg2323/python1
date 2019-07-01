# 구구단 출력

i, dan = 0,0
for i in  range(2,10):
    guguLine = guguLine + ("# %d단 #" % i)

print(guguLine)


for i in range (1, 10):
    guguLine =""
    for k in range(2,10):
        guguLine = guguLine + str("%2dX  %2d = %2d" % (k, i, k*i))
    print("%d X %d = %2d" % (dan, i, dan * i))
