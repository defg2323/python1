def func1():
    global a
    a = 10
    print("func1()에서 a값 %d"%a)

def func2():
    print("func1()에서 a값 %d" %a)
    print("func1()에서 b값 %d" %a)
    return (True)

def telcheck(aaa):
    print (aaa)
    if len(aaa) < 11:
        return  (True)

if __name__ =="__main__":
    result = False

    tel1 = "010-4088-0"
    tel2 = "010-4088-0116"

    tel1 = tel1.replace('-','')
    tel2 = tel2.replace('-','')
    result = telcheck(tel2)

    if result ==True:
        print("핸드폰 전화번호 형식에 맞음")
    else:
        print("핸드폰 전화번호 형식에 맞지 않음")

