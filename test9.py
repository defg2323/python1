import sys

intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8

if __name__ == "__main__":
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print('int 형 기본 크기 -->', sys.getsizeof(intVar))
    print('float 형 기본 크기 -->', sys.getsizeof(floatVar))
    print('bool 형 기본 크기 -->', sys.getsizeof(boolVar))
    print('str 형 기본 크기 -->', sys.getsizeof(strVar))
    print('list 형 기본 크기 -->', sys.getsizeof(listVar))
    print('tuple 형 기본 크기 -->', sys.getsizeof(tupleVar))
    print('dictionary 형 기본 크기 -->', sys.getsizeof(dictVar))
    print('set 형 기본 크기 -->', sys.getsizeof(setVar))