import test35

def para3_func(v1,v2,v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = test35.para2_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d"%hap)
hap = para3_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d"%hap)