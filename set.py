
num1 = {1,2,3,4}
num2 = set([5,6,7,8])

num2.add(9)
num2.remove(9)
print(num1)
print(num2)
print(9 in num2)
print(5 in num2)
print(5 not in num2)

print(num1 | num2)  # union
print(num1 & num2)  # intersection
print(num1 - num2)  # difference