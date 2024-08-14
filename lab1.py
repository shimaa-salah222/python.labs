# question 1------------------
""" 
s = 'shimaa'
count = 0
for char in s:
    if char.lower() in "aeiou":
        count += 1
print("Number of vowels:", count) """

#question 2------------------

""" def generate_array(length, start):
    return list(range(start, start + length))

print(generate_array(5, 1))
print(generate_array(7, 10)) """

#question 3----------------
""" l = input("enter 5 elements: ")
l=[int(i) for i in l.split()]
l.sort(reverse=True)
print("array in desc: ",l)
l.sort()
print("array in asc: ",l)  """


#question 4------------------

""" def fizz_buzz(num):
    
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
       
        else:
             print(num)

print(fizz_buzz(15))  
print(fizz_buzz(9))  
print(fizz_buzz(7))  
print(fizz_buzz(40))  
print(fizz_buzz(27))  """ 


#question 5------------------

""" def re_string(s):
     print(s[::-1])

x_input = input("inter string: ")
print(re_string(x_input))   """ 


#question 6-----------------

""" def palindrome(s): 
    s = s.replace(" ", "").lower()  
    return s == s[::-1]

print(palindrome("madam"))
print(palindrome("radar radar"))
print(palindrome("Hello"))  """ 

#question 7-----------------------

""" def longest_string(s):
    max_length = 0
    max_substring = ""
    current_length = 1
    current_substring = s[0]

    for i in range(1, len(s)):
        if ord(s[i]) > ord(s[i-1]):
            current_length += 1
            current_substring += s[i]
        else:
            if current_length > max_length:
                max_length = current_length
                max_substring = current_substring
            current_length = 1
            current_substring = s[i]

    if current_length > max_length:
        max_length = current_length
        max_substring = current_substring

    print(f"Longest substring is: {max_substring}")
longest_string('abdulabcxyz') """