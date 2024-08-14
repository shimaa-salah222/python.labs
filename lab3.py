#problem---------------------------
""" def largestdif(num):
    str_num=str(num)
    digits = sorted([int(d) for d in str_num])
    largest = int(''.join(map(str, digits[::-1])))
    smallest = int(''.join(map(str, digits)))
    return largest - smallest
print(largestdif(231)) """

#lab3----------------------------
#question 1----------------------

""" with open ("file1.txt","r") as file:
   lines = [line.strip() for line in file.readlines()]
print(lines) """

#question 2------------------------------

""" list =["Hello", "World", "This", "is", "a", "test"]
list.append("shimaa")

with open("file1.txt","a") as file:
    for item in list:
        file.write(item + "\n") """

#question 3---------------------
""" from calculator.my_functions import *
result1 = sum(2, 3)
result2 = subtract(5, 2)
result3 = divide(6, 3) 
result4 = multiply(4, 5)

print(result1,result2,result3,result4) """


#question4------------------------
from calculator.my_functions2 import sum, subtract, divide, multiply

