# function1.py


def setValue(newValue):
    x = newValue
    print("지역변수:", x)


#함수를 호출
retValue = setValue(10)
print(retValue)


#함수를 정의
def swap(x,y):
    return y,x


#호출
print(swap(3,4))


def intersect(prelist, postlist):
    #지역 변수(List)
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result



#호출
print(intersect("HAM","SPAM"))



#기본값을 명시
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#지역 변수와 전역 변수

x = 5
def func1(a):
    return a+x


#호출
print(func1(1))


def func2(a):
    #지역변수
    x = 1
    return a+x

#호출
print(func2(1))

#가변인자 함수

    def union(*ar):
        #지역 변수
        result = []
        for item in ar:
            for x in item:
                if x not in result:
                    result.append(x)
        return result

    #호출
    print(union("HAM","EGG"))
    print(union("HAM","EGG","SPAMM"))


