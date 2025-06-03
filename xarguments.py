
def student(*details):
    print(details)

student(101,"Asma",3.75)
student(102,"Israt",3.75)


def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
add(10,20)
add(10,20,30)
add(10,20,30,40)