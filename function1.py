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