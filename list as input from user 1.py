n = input ("Enter a text of number: ")
# 10 20 30

list = n.split()  # 10,20,30
sum = 0

for num in list:
    sum = sum + int(num)

print(sum)