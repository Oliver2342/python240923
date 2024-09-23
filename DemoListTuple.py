

strA = "파이썬은 강력해"
strB = "python is very powerful"
x = 100
y = 3.14


print(dir())
print(len(strA))
print(len(strB))


strC = """다중 라인을
저장하는 경우는
이렇게 처리
"""
print(strC)


#슬라이싱
print(strA[0])
print(strA[0:3])
print(strA[-2:])
print(strA[-3:])


colors = ["red","green"]

colors.append("white")
print(colors)



lst = ["red","blue","green"]
print(lst)
lst.append("white")
print(lst)
lst.insert(1, "pink")
print(lst)
lst.remove("blue")
print(lst)
lst.sort()
lst.reverse()


#Set 형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))



