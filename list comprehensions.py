
#map to list comprehensions
#easy way
num = [1,2,3,4,5,6,7,8]
result = [x*x for x in num]
print (result)


#filter to list comprehension
#easy way
num = [ 1,2,3,4,5,6,7,8,9]
result = [x for x in num if x%2==0]
print (result)