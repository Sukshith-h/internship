#!/usr/bin/env python
# coding: utf-8

# # python first program
# print("Hello Python")

# #lines and indentation
# if True: 
#     print ("True") 
# else: 
#   print ("False") 
# #indentation may be used insted of {}

# # Multiline: python use "\" this as a line continuation charecter to denote that the line is to be continued
# one=5
# two=6
# three=1
# total=one+\
#       two+\
#       three
# print(total)

# # the statement contained within any of braces do not use line continuation character
# #eg: tuples,lists,set,dictionaries etc
# my_list=[1,2,3,
#         4,5]

# In[5]:


print(my_list)


# # Quotations in python:python uses (')/(")/(""") to denote string literals
# s="sukshith"
# print(s)
# 

# # The triple quotes are used to span the strings over multiple lines
# s="""this is a sentence....
# and it uses the multiline"""
# print (s)

# # Waiting for the user: the following code displays the promt saying "press enter key to exit" and then waits for the user's action
# #!/usr/bin/python3 
# input("\n\nPress the enter key to exit.") 

# In[9]:


#!/usr/bin/python3 
input("\n\nPress the enter key to exit.") 


# # Multiple statements on a single line :  it is allowed by using semicolon(;)
# import sys; x=5; y=5; sum=x+y; print(sum)

# # Command Line Arguments::Many programs can be run to provide you with some basic information about how they should be run. Python enables you to do this with -h:
# #$ python -h 
# #usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ... 
# #Options and arguments (and corresponding environment variables): 
# #-c cmd : program passed in as string (terminates option list) 
# #-d     : debug output from parser (also PYTHONDEBUG=x) 
# #-E     : ignore environment variables (such as PYTHONPATH) 
# #-h     : print this help message and exit 
# # The getopt that helps you to parse command line arguments
# # $ python test.py arg1 arg2 arg 3
# # sys module provide access to any commandline arguments via sys.argv
# #len(sys.argv)-- provides length
# 

# In[13]:


#!/usr/bin/python3 
import sys 
print ('Number of arguments:', len(sys.argv), 'arguments.') 
print ('Argument List:', str(sys.argv)) 


# In[15]:


print("over")


# # parsing command line arguments:
# #mgetopt module helps you to parse commandline arguments
# # Syntax: getopt.getopt(args,options,[long_options])

# # Python variables
# # variables are reserved memory locations to store values
# # Based on the datatype of a variable,the interpreter allocates memory and decides what can be stored
# # by assigning to different data types we can store integers,characters,decimals etc
# 

# # Assigning values to Variables
# # python variable donot need explicit declaration
# # declaration happens automatically when you assign value to variable
# count=100        # integer assignment
# miles=25.5       # floating point 
# name="sukshith"   # String
# print(count,miles,name)

# # Multiple assignments:
# # python allows you to assign single values to several variables
# a=b=c=1
# print ("a=",a,"b=",b,"c=",c)

# #  You can also assign multiple objects to multiple variables:
# a,b,c=1,2,"sukshi"
# print("a is", a)

# # Standard data types: python has 5 standard datatypes
# #  numbers
# #  String
# #  list
# #   tuples
# #  Dictionary
# 

# # python numbers:
# #number datatype stores numeric values
# var1=20
# var2=50
# print(var1)

# # you can also delete reference to a number object by using del statement 
# # Syntax:: del var1[,var2[var3[....varN]]]
# del var1

# In[35]:


var2


# In[36]:


var1


# In[37]:


var1=20


# In[38]:


del var1,var2


# # python supports 3 different numerical types::
# #int,float,complex
# 

# # python Strings
# #strings in python is identified as a contigious set of characters and represented in quotation mark
# # quotes may bre single or double 
# # strings can be concatinated by using + symbol and * is repetition operator
# str = 'Hello World!' 
# print (str)----># Prints complete string 
# print (str[0])----># Prints first character of the string 
# print (str[2:5])---># Prints characters starting from 3rd to 5th 
# print (str[2:])----># Prints string starting from 3rd character 
# print (str * 2)----># Prints string two times 
# print (str + "TEST")---># Prints concatenated string 

# # python lists:: 

# A list is the collection of items. The elements in python are seperated by commas and enclosed within square brackets.. for some extenct lists are similar to arrays in python
# # The main differnce is that list may contain elements of different data type.

# In[1]:


list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]


# In[2]:


list


# In[3]:


print(list)  #prints the complete string
print(list[0]) #prints the element which is int 0th position


# In[4]:


print(list[1:3])  #prints the element starting from 1st position till 3rd;


# In[5]:


print(list[2:])  #prints the item from 2nd position to the end of list


# In[7]:


tiny_list=['1','ram']


# In[8]:


print(list+tiny_list)   #concatinates the two lists


# # python tuples:: the tuple is another sequesnce of data type similar to list:

#  tuple consists of a no of values seperated by commas,tuples are different from list by they are enclosed by paranthasis and cannot be updated..

# In[10]:


tuple1=('abcd',2,3.5,4)


# print(tuple)

# In[11]:


print(tuple1)


# In[12]:


print(tuple1[0])


# In[16]:


print(tuple1[1:3])


# In[17]:


print(tuple1[1:])


# # PYTHON DICTIONARIES

# # python dictionaries are enclosed by curly braces{} 

# # ex:

# In[26]:


dict_1={ 'name':'sukshith', 'usn':'4su17cs103','branch':'cse'}


# In[28]:


print(dict_1)


# In[34]:


print(dict_1.keys())


# In[35]:


print(dict_1.values())


# # Data type conversion

#  there are several builtin functions to perform conversion from one datatype to another

# x=5
# int(x[,base]

# In[38]:


float(x)


# In[39]:


str(x)


# repr(x)

# In[47]:


chr(x)   #converts to character


# In[52]:


hex(x)  #converts integer to hexadecimal string


# In[53]:


oct(x)  #converts integer to an octal string


# # python basic operators

# operators are the constraints which manipulates the value of operands

# ---> Types of operators

# * Arithmetic operators

# * comparision/relational operators

# * assignment operators

# * logical operators

# * bitwise operators

# * membership operators

# * identity operators

# #  Python Arithmetic operators

# In[57]:


a=10
b=21
print(a+b)
print(a*b)
print(a-b)
print(a%b)
print(a**b)


# #  Python comparision operators

# * ==  equal to

# * !=   not equal to

# * ">" greater than

# * '<'  less than

# * '>=' greater than equal to

# *  '<=' less than equal to

# In[59]:


a=10
b=9
a==b


# In[60]:


a!=b


# In[61]:


a>b


# In[62]:


a<b


# # Python assignment operator

# In[63]:


a=b


# In[64]:


a=10
b=20


# In[65]:


a=b


# In[66]:


a


# In[67]:


b


# In[69]:


a+=b


# In[70]:


a


# In[72]:


a-=b


# In[73]:


a


# In[74]:


a*=b


# In[75]:


a


# In[76]:


a/=b


# In[77]:


a


# # Python bitwise operator

# Bitwise operator works on bits and performs bit-by-bit operation

# In[79]:


a=1
b=1


# In[80]:


a&b


# In[81]:


a|b


# In[82]:


a^b


# In[83]:


~ a


#  Python's built-in function bin() can be used to obtain binary representation of an integer number

# In[84]:


a>>b


# In[85]:


a<<b


# # Python Logical operators

# In[86]:


a=1
b=2
a and b


# In[88]:


a or b


# In[89]:


not(a and b)


# # Python Membership Operators 

# * in and notin

# # python identity operators

# is and is not

# # python operators precedence

# 1) **
# 2)~ + -
# 3) */%//
# 4) + -
# 5) >><<
# 6)&
# 7) ^|
# 8)<=<>>=
# 9) <>==!=

# # Python conditional statements:

# # if statement:

# if expression:
# 
#     statement

# # if...elif...else statements:

# if expression:
#     
#     statement(s)
#     
# else:
#         
#         statement(s)

# In[108]:


a=int(input(" enter the value of a\n"))
b=int(input("enter value of b\n"))
if a>b:
        print("a is greater")
else:
        print("b is greater")
    


# # The elif statements:
# 

#  if exression1:
#     
#     statement(s)
#     
# elif expression2:
#     statement(s)
#     
# else:
#     
#     statement(s)
#     

# # example:

# In[94]:


#!/usr/bin/python3 
amount=int(input("Enter amount: ")) 
 
if amount<1000: 
    discount=amount*0.05 
    print("Discount",discount) 
elif amount<5000: 
    discount=amount*0.10 
    print ("Discount",discount) 
else: 
    discount=amount*0.15 
    print ("Discount",discount)
    print ("Net payable:",amount-discount)


# # nested if statements

# There may be a situation where u want to check another condition after a condition resolves to true

# if expression1:
#     
#     statement(s)
#     
#     if expression2:
#         
#         statement (s)
#     elif expression3:
#         
#         statement(s)
#     else:
#         statement(s)
#     

# In[119]:


num=int(input("enter the number\n"))
if num%2==0:
        if num%3==0:
            print("divisible by both 2 and 3\n")
        else:
            print("only divisible by 2")
else:
     if num%3==0:
            print("only divisible by 3\n")
     else:
            print("not divisible by both")


# # single statement suits

# In[126]:


var=100
if var==100: print("good")
print("well")


# # Python loops:

# it is used when we want to execute the block of code several number of times

# # types of loops :

# * while

# * for

# * nested loops

# # 1) while loop

# A while loop executes the set of statements repeatedly as long as the condition is true.

# Syntax:

# while expression:
# 
#     statement(s)

# statement(s) may be single or block of statements

# # example:

# In[ ]:


count=0
while (count<=9):
    print("count:",count)
    count=count+1
print("bye")


# # the infinite loop:

# A loop becomes infinite loop if a condition never becomes false

# # example:

# In[ ]:


var = 1 
while var == 1 :  # This constructs an infinite loop 
   num = int(input("Enter a number  :")) 
   print ("You entered: ", num) 
print ("Good bye!") 


# # using else statements with loop :

# * if the else statement is used with while loop, it gets executed when condition becomes false

# ex:

# In[ ]:


count = 0 
while count < 5: 
   print (count, " is  less than 5") 
   count = count + 1 
else: 
   print (count, " is not less than 5"


# 0 is less than 5 
# 
# 1 is less than 5
# 
# 2 is less than 5
# 
# 3 is less than 5
# 
# 4 is less than 5
# 
# 5 is not less than 5 
# 

# * while loop also supports single statement

# # for loop:

# syntax:

# for iterating_var in sequence:
# 
#     statements(s)

# # The range() function:

# The built-in function range() is the right function to iterate over a sequence of numbers.

# In[ ]:


range(5)


# range(0,5)

# In[ ]:


list(range(5))


# [0, 1, 2, 3, 4] 

# In[ ]:


for var in lis(range(5)):
    print(var)


# 0
# 
# 1
# 
# 2
# 
# 3
# 
# 4

# In[ ]:


for letter in 'python':
    print('current Letter :',letter)


# Current Letter : P
#     
# Current Letter : y
#     
# Current Letter : t
#     
# Current Letter : h 
#     
# Current Letter : o 
#     
# Current Letter : n

# # Iterating by Sequence Index 

# In[ ]:


fruits = ['banana', 'apple',  'mango'] 
for index in range(len(fruits)): 
   print ('Current fruit :', fruits[index]) 
print ("Good bye!")


# Current fruit : banana 
# 
# Current fruit : apple 
# 
# Current fruit : mango
# 
# Good bye!

#  If the else statement is used with a for loop, the else block is executed only if for loops terminates normally (and not by encountering break statement). 
#  

# * nested loops are allowed:

# # loop control statements:

# # break statement:

# terminates the loop statement and transfers execution to the statement immediatly following the loop

# # continue statement 

# causes the loop to skip the remainder of its body and immediatly retest its condition prior to reiterating

# # Pass statement

# The pass statement in python is used when a statement is required syntactically but you do not want any command or code to execute

# # break statement:

# # Syntax:

# break

# In[1]:


for letter in 'Python':     # First Example 
   if letter == 'h': 
      break 
   print ('Current Letter :', letter) 


# # continue statement:

# In[2]:


for letter in 'Python':     # First Example 
   if letter == 'h': 
      continue 
   print ('Current Letter :', letter)


# # Pass statement:

# In[3]:



 
for letter in 'Python':  
   if letter == 'h': 
      pass 
      print ('This is pass block') 
   print ('Current Letter :', letter) 
 
print ("Good bye!") 


# # Iterator and Generator:

# In[18]:


get_ipython().system('usr/bin/python3')
import sys 
def fibonacci(n): #generator function 
    a, b, counter = 0, 1, 0 
    while True: 
        if (counter > n):  
            return 
        yield a 
        a, b = b, a + b 
        counter += 1 
f = fibonacci(5) #f is iterator object 
 
while True: 
   try: 
      print (next(f), end=" ") 
    except StopIteration: 
      sys.exit() 


# iterator is an object which allows a programmer to traverse through all the elements of a collection ,regardless of its specific implementation..in python the iterator object implements two methods,iter() and next().

# In[7]:


import sys
list =[1,2,3,4]
it=iter(list)    # this builds an iterator object
print(next(it))   #prints next available element in iterator
for x in it:
    print(x,end=" ")


# In[9]:



import sys
list =[1,2,3,4]
it=iter(list)    # this builds an iterator object
print(next(it))
while True: 
   try: 
      print (next(it)) 
   except StopIteration: 
      sys.exit()


# In[10]:


import sys
list =[1,2,3,4]
it=iter(list)    # this builds an iterator object
print(next(it))


# a generator is a function that produces or yields a sequence of values using yeild method

# when generator function is called it returns a generator object without even begining execution of the function . when the next() method is called for the first time ,the function starts executing ,untill it reaches the yeild statement

# In[14]:


get_ipython().system('usr/bin/python3')
import sys
def fibonacci(n):   # generator function
    a,b,counter=0,1,0
    while True:
        if(counter >n):
            return
        yield a
        a,b=b,a+b
        counter +=1
f=fibonacci(5)  # f is iterator object
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()


# # Python datatypes:

# number data types store the numeric values.They are immutable data types.this means changing the values of a number data types results in a newly allocated object

# * number objects are created when you assign a value to them

# In[15]:


var1 =1 
var2=10


# * you can also delete the object using del statement. 

# syntax:

# del var1[,var2[,var3[.....,varn]]]]

# * different numeric types:

# * int(signed integers): positive or negetive whole numbers with no decimal point

# * float : floating point or decimal point numbers....float may also be in scientific notations like E or e indicating the power of 10.

# * complex (complex numbers):

# are of the form a+bj where a and b are floats and j represents the squareroot of -1(which is an imaginary number)

# # number type conversion :
# 

# * type int(x) to convert x to plain integer.

# * type float(x) converts x to floating point

# * type complex(x) converts x to complex number with x as real part and imaginary part will be 0.

# * type complex(x,y) x--> real part and y -->imaginary part

# In[17]:


x=9.8
int(x)


# In[18]:


float(x)


# In[19]:


complex(x)


# In[20]:


y=2


# In[21]:


complex(x,y)


# # mathamatical functions:

# # * abs(x) to absolute value of x: the positive distance between x and zero

# In[22]:


x=9.8


# In[23]:


abs(x)


# In[26]:


y=10


# In[32]:


import math
math.fabs(x)


# In[34]:


math.ceil(x)    # smallest integer not less than x


# In[37]:


math.exp(x)    # performs e**x


# In[40]:


math.floor(x)  # largest integer not greater than x


# In[41]:


math.log(x)


# In[42]:


math.log10(x)


# In[44]:


max(x,y)


# In[45]:


x=7
y=9
z=10


# In[46]:


min(x,y)


# In[47]:


math.modf(x)


# In[48]:


math.pow(x,y)


# In[49]:


math.sqrt(x)


# In[57]:


round(70.23456)


# # The anonymous Functions:

# The functions are called anonymous because they are not declared in the standard manner by using the def keyword.

# * you can use the  lambda keyword to create small anonymous functions.

# * lambda forms can take any number of arguments but return just one value in the form of an expression.They cannot contain commands or multiple expressions.

# * lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace

# * Syntax:

# lambda [arg1 [,arg2,....argn]]:expression

# In[59]:


sum= lambda arg1,arg2:arg1+arg2
print("value of total:", sum(10,20))
print("value of total:",sum(20,20))


# # filter() :

# * The filter() method constructs an iterator from elements of an iterable for which the function returns true.

# * it tests each element in the iterable to be true or not

# # syntax:

# filter(function,iterable)

# * function that tests if elements of an iterable returns true or false

# * iterable: iterable which is to be filtered

# it could be sets,lists,tuples

# In[68]:


#list of alphabets
alphabets=['a','b','c','d','e','f','g','h','i','o']
#function that filter vowels
def filterVowels(alphabet):
     vowels=['a','e','i','o','u']
if(alphabet in vowels):
    return True
else:
    return False
    filteredVowels=filter(filterVowels,alphabets)
    print("filtered vowels are:")
for vowel in filteredVowels:
    print(vowel)


# # map():
# 
