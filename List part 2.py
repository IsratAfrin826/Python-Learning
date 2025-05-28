subjects = ["C" , "C++" , "Java" , "Python" , "Basic"]
print (len(subjects))

subjects.append("TOC")
print(subjects)

subjects.insert(2,"OS")
print(subjects)

subjects.remove("Basic")
print(subjects)

num =[20,10,4,55]
num.sort()
print(num)

num =[20,10,4,55]
num.reverse()
print(num)

num =[20,10,4,55]
num.pop()
num.pop()
print(num)

num =[20,10,4,55]
num.clear()
print(num)

num =[20,10,4,55]
num2 = num.copy()
print(num2)

num =[20,10,4,55]
pos = num.index(4)
print(pos)

num =[20,10,4,55,4,4]
pos = num.count(4)
print(pos)




