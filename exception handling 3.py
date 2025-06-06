try:
    num1 = int(input("Enter first number : "))
    num2= int(input("Enter second number : "))
    result = num1 / num2
    print(result)

#except (ValueError,ZeroDivisionError):
       #print("you have entered incorrect input.")
except ValueError:
    print("you have to insert only integer.")
except ZeroDivisionError:
    print("you can not divide a number by 0 ")
finally:
    print("Thanks !!!")