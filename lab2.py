#question 1--------------------------
""" def check(num):
       if num in range (-5, 5):
              return True
       else:
              return False
       
print(check(2))      
print(check(6))      
print(check(-1))      
print(check(-6))  
 """

#question 2---------------------------
""" l1=['name','age','country']
l2=['shimaa',20,'egypt']

dic = dict(zip(l1, l2))

print(dic) """

#question3---------------------------
""" def square_list():
    li=[i**2 for i in range(1,31)]
    print(li)

square_list()  """ 
#question4---------------------------

li=[3, 6, 4, 0, 8]
print(li)
li.pop(4)
print(li)
li.insert(1,'R')
print(li)

num = (input("Enter a number or string to delete: "))
while True:
    if num in li:
        li.remove(num)
        print(li)
        break
    else:
        print(num, "is not found in the list")
        break


#question 5------------------------------------

""" dict1={'name':'mona','age':30,'city':"ismailia"}
dict2={'job':'engineer','department':'it','salary':2000}

combined_dict = dict(list(dict1.items()) + list(dict2.items()))

print(combined_dict) """