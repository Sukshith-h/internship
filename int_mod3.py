#!/usr/bin/env python
# coding: utf-8

# # String

# Strings can be created simply by enclosing them in ""/''.

# In[1]:


var1='hello'
print (var1)


# * accessing values in Strings:

# To access substrings use brackets for slicing/indexing.

# In[5]:


var1='hello world'
var2="pythonprogramming"
print("var1[0]:",var1[0])
print("var2[1:5]:",var2[1:5])


# # Updating Strings 

# You can "update" an existing string by (re)assigning a variable to another string. The new value can be related to its previous value or to a completely different string altogether.
# 
# For example-

# In[6]:


var1='hello world'
print('updated string is',var1[:6]+'python')


# # String special operations:

# + concatination
# 
# * repetation
# 
# []  indexing
# 
# [:] slicing 
# 
# in returns true if character exists in given String
# 
# not in  returns true if character does not exist in the given String
# 
# r/R  raw string
# 
# % to perform string formating

# # string formating:

# In[7]:


print("my name is %s and my weight is %d kg" %('sss',30))


# %c for character
# 
# %s string 
# 
# %i and %d decimal integer
# 
# %u unsigned decimal integer
# 
# %o octal integer 
# 
# %x hexadecimal integer(lower case)
# 
# %X hexadecimal integer(upper case)
# 
# %e exponential notation(lower case)
# 
# %E exponential notation(upper case)
# 
# %f floating point real numbers
# 
# 

# # Unicode Strings:

# * capitalize()  capitalizes first letter of string
# 
# * center(width,fillchar)  Returns a string padded with the original string centered to a total of width columns
# 
# * count(str, beg=0,end=len(string)) counts how many times str occurs in string or substring if starting index beg and index end is given.
# * decode(encoding='UTF-8',errors='strict') decodes the string using codec registered for encoding
# 

# In[1]:


str = "this is string example....wow!!!" 
print ("str.capitalize() : ", str.capitalize())


# # string center() method

# str.center(width[fillchar])

# width - this is total width of the string.
# 
# filler - this is filler character.

# # string count method:

# * returns no of occurances of substring sub in range[start,end]
# 
# * syntax:
#     
#     str.count(sub,start=0,end=len(string))
#     
# * sub: substring to be searched.

# In[4]:


str="this is string example....wow!!!"
sub='i'
print("str.count(i):",str.count(sub))
sub='exam'
print("str.count('exam',10,40):",str.count(sub,10,40))


# # string decode() method:

# The decode() method decodes the string using the codec registered for encoding. It defaults to the default string encoding. 

# Syntax:

# str.decode(encoding='utf-8',errors='strict')

# In[8]:





# # String endswith() Method :

# It returns True if the string ends with the specified suffix, otherwise return False optionally restricting the matching with the given indices start and

# Syntax:

# str.endswith(suffix,start,end)

# In[16]:


str="this is string example....woww!!!"
suffix='!'
print(str.endswith(suffix))
print(str.endswith(suffix,0,32))
print(str.endswith(suffix,10,20))


# # string find()method:
#     
#     

# The find() method determines if the string str occurs in string, or in a substring of string if the starting index beg and ending index end are given. 

# Syntax :

# str.find(str,beg=0 end=len(string))

# * "if str found returns the index .....otherwise returns -1"

# In[18]:


str1="this is string example"
str2='exam'
print(str1.find(str2,10,20))
print(str1.find(str2,0,20))
print(str2.find(str1))
print(str1.find(str2,30,40))


# # string index() method:

# The index() method determines if the string str occurs in string or in a substring of string, if the starting index beg and ending index end are given. This method is same as find(), but raises an exception if sub is not found. 
# 

# syntax:   str.index(str,beg=0 end=len(string))

# In[19]:


str1 = "this is string example....wow!!!" 
str2 = "exam"; 
print (str1.index(str2)) 
print (str1.index(str2, 10)) 
print (str1.index(str2, 40))


# # string isalnum() method:

#  the isalnum() method checks weather the string consists of alphanumeric characters or not

# str.isalnum()

# In[22]:


str="kk16"
print(str.isalnum())


# In[27]:


str="sukshi is good"
print(str.isalnum())


# * The isalpha() method checks whether the string consists of alphabetic characters only

# In[28]:


str="sukshi"
print(str.isalpha())


# In[29]:


str="5658"
print(str.isalnum())


# In[30]:


str ="578"
print(str.isdigit())


# In[31]:


str="hs9"
print(str.isdigit())


# # string islower()method:

# The islower() method checks whether all the case-based characters (letters) of the string are lowercase

# In[34]:


str="This is computer"
print(str.islower())


# In[35]:


str="this is python"
print(str.islower())


# # string isnumeric() method:

# The isnumeric() method checks whether the string consists of only numeric characters. This method is present only on unicode objects. 

# In[42]:


str="sukshi2103"
print(str.isnumeric())
str1="3444565"
print(str1.isnumeric())


# # String isspace() Method 

# The isspace() method checks whether the string consists of whitespace.. 

# In[44]:


str = "       "  
print (str.isspace()) 
str = "This is string example....wow!!!" 
print (str.isspace()) 


# # String istitle() Method:

# In[45]:


str="Sukshi Is Good"
str2="Sukshi is goood"
print(str.istitle())
print(str2.istitle())


# # string isupper() method:

# In[46]:


str="SUKSHI"
print(str.isupper())
str1="SUKSHi"
print(str1.isupper())


# # string join() method:
#     

# The join() method returns a string in which the string elements of sequence have been joined by str separator. 
# 
# Syntax :

# str.join(sequence)
# 
# sequence - This is a sequence of the elements to be joined

# In[48]:


ssss="."
seq=("a","b","c")
print(ssss.join(seq))


# # String len() Method

# The len() method returns the length of the string

# In[52]:


str = "this is string example....wow!!!" 
print ("Length of the string: ", len(str))


# # String lower() Method 

# This method returns a copy of the string in which all case-based characters have been lowercased

# In[53]:


str = "THIS IS STRING EXAMPLE....WOW!!!" 
print (str.lower()) 


# # String maketrans() Method

# # This method returns a translate table to be used translate() function

# The following example shows the usage of maketrans() method. Under this, every vowel in a string is replaced by its vowel position − 
# 

# In[57]:


intab = "aeiou" 
outtab = "12345" 
trantab = str.maketrans(intab, outtab) 
str = "this is string example....wow!!!" 
print (str.translate(trantab)) 


# # String max() Method:

# The max() method returns the max alphabetical character from the string str.

# In[58]:


#!/usr/bin/python3 
str = "this is a string example....really!!!" 
print ("Max character: " + max(str)) 
str = "this is a string example....wow!!!" 
print ("Max character: " + max(str))


# # String min() Method :

# The min() method returns the min alphabetical character from the string str. 

# In[59]:


str = "www.tutorialspoint.com" 
print ("Min character: " + min(str)) 
str = "TUTORIALSPOINT" 
print ("Min character: " + min(str)) 


# # String replace() Method 

# This method returns a copy of the string with all occurrences of substring old replaced by new. If the optional argument max is given, only the first count occurrences are replaced. 

# # Syntax :
# 
# str.replace(old, new[, max]) 

# In[62]:


str = "this is string example....wow!!! this is really string" 
print (str.replace("is", "was")) 
print (str.replace("is", "was", 2)) 


# # lists:

# list contains the elements enclosed within the square brackets[]
# . Important thing about a list is that the items in a list need not be of the same type. 
# Creating 

# In[63]:


list1 = ['physics', 'chemistry', 1997, 2000];


# In[64]:


print(list1)


# # Accessing Values in Lists :

# To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that inde

# In[66]:


list1 = ['physics', 'chemistry', 1997, 2000];
print(list1[0])
print(list1[1:3])


# # updateing the lists:

# You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operato

# In[67]:


list = ['physics', 'chemistry', 1997, 2000] 
print("present value is:",list[2])
list[2]=2000
print("updated value is ",list[2])


# # Delete List Element:
#     

# In[70]:


print(list)
del list[2]
print(list)


# # Basic List Operations:

# Lists respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string

# In[77]:


list=[1,2,3,4,5]
print(len(list))
list=list+[6,7,8,9,10]
print(list)
list1=2*list
print(list1)
print(list*3)
print(3 in list)
for x in list:
    print(x)
    x=x+1


# # indexing and slicing:

# In[79]:


list=['sukshi',1,2,3]
print(list[0])
print(list[0:3])
print(list[0:3:2])


# # Built-in List Functions & Methods :

# # List len() Method :

# The len() method returns the number of elements in the list

# In[83]:


list1 = ['physics', 'chemistry', 'maths'] 
print (len(list1)) 


# # List max() Method:

# The max() method returns the elements from the list with maximum value:

# In[84]:


list1, list2 = ['C++','Java', 'Python'], [456, 700, 200] 
print ("Max value element : ", max(list1)) 
print ("Max value element : ", max(list2)) 


# # List min() Method

# This method returns the elements from the list with minimum value.

# In[85]:


list1, list2 = ['C++','Java', 'Python'], [456, 700, 200] 
print ("min value element : ", min(list1)) 
print ("min value element : ", min(list2)) 


# # List list() Method:

# The list() method takes sequence types and converts them to lists. This is used to convert a given tuple into list.

# Syntax:
#     
# list( seq ) 

# In[87]:


aTuple = (123, 'C++', 'Java', 'Python') 
list1 = list (aTuple) 
print ("List elements : ", list1) 


# In[98]:


list1=['sukshi','jade',1,2,3,4,5]
list1.append('jackie')
print(list1)
 
    
list1.count('sukshi')

list1.extend('21')
print(list1)


# In[99]:


list1[2]


# In[103]:


list1.insert(0,21)
print(list1)


# In[105]:


list.pop(0)


# In[108]:


list1.remove(1)
print(list1)


# In[113]:


list2=[1,2,3,4,5]
list2.reverse()
print(list2)


# In[115]:


list2.sort()
print(list2)


# In[116]:


list1.sort()
print(list1)


# # Tuples:

# In[2]:


tup1 = ('physics', 'chemistry', 1997, 2000) 
print(tup1)


# In[5]:


tup1 = ('physics', 'chemistry', 1997, 2000)
print(tup1[0])
print(tup1[1:3])


# In[6]:


tup2=(1,2,3,4,5,6,7,8,9)
print(tup2[1:9:2])


# In[10]:


tup1 = (12, 34.56) 
tup2 = ('abc', 'xyz') 
tup3=tup1+tup2
print(tup3)


# # Delete Tuple Elements:
# 

# In[15]:


tup4=(1,2,3,4,5,6,7,8)
print(tup4)
del tup4
print("after deleting tuple:",print(tup4))


# # Basic Tuples Operations :

# # Tuple len() Method:

#  The len() method returns the number of elements in the tuple.

# In[16]:


tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc') 
print ("First tuple length : ", len(tuple1)) 
print ("Second tuple length : ", len(tuple2))


# Tuple max() Method :

# The max() method returns the elements from the tuple with maximum value:

# In[17]:


tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200) 
print ("Max value element : ", max(tuple1)) 
print ("Max value element : ", max(tuple2))


# Tuple min() Method:

# In[18]:


tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200) 
print ("min value element : ", min(tuple1)) 
print ("min value element : ", min(tuple2))


# # Tuple tuple() Method :

# The tuple() method converts a list of items into tuples. 

# In[19]:


list1=['sukshi','ssss','dddd']
tuple1=tuple(list1)
print(tuple1)


# # Dictionary:

# Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}. 

# In[20]:


dict={'apple':'fruit','bike':'vehicle','kgf':'movie'}
print(dict)


# In[21]:


dict['apple']


# In[24]:


dict.keys()


# In[25]:


dict.values()


# In[26]:


dict.items()


# # Updating Dictionary :

# In[27]:


dict ={'name':'sukshi','age':19,'class':'cseb'}
dict['age']=20;
dict['school']="dps school"
print(dict['age'])
print(dict)


# # Delete Dictionary Elements:

# In[28]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
 
del dict['Name']
dict.clear() 
del dict 
print(dict)


# # Properties of Dictionary Keys :

# Dictionary len() Method :

# This method returns the length. 

# In[31]:


dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'} 
print ("Length : ", len (dict))


# # Dictionary str() Method:

# The method str() produces a printable string representation of a dictionary

# In[33]:


dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'} 
print ("Equivalent String :", str (dict))


# # Dictionary type() Method :

# The method type() returns the type of the passed variable. If passed variable is dictionary then it would return a dictionary type. 

# In[34]:


dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'} 
print ("Variable Type : " ,  type (dict)) 


# # Dictionary clear() Method 

# The method clear() removes all items from the dictionary. 

# In[35]:


dict = {'Name': 'Zara', 'Age': 7} 
print ("Start Len :" ,  len(dict)) 
dict.clear() 
print ("End Len :", len(dict))


# # Dictionary copy() Method:

#  The method copy() returns a shallow copy of the dictionary. 

# In[36]:


dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'} 
dict2 = dict1.copy() 
print ("New Dictionary : ",dict2)


# # Dictionary fromkeys() Method:

# The method fromkeys() creates a new dictionary with keys from seq and values set to value. 

# dict.fromkeys(seq[, value]))

# In[39]:


seq =('name','age','sex')
dict=dict.fromkeys(seq)
print(dict)
dict=dict.fromkeys(seq,19)
print(dict)


# # Dictionary get() Method 

# The method get() returns a value for the given key. If the key is not available then returns default value None.

# dict.get(key, default=None) 

# In[40]:


dict = {'Name': 'Zara', 'Age': 27} 
print ("Value : ",  dict.get('Age')) 
print ("Value : " , dict.get('Sex', "NA"))


# # Dictionary items() Method :

# *The method items() returns a list of dict's (key, value) tuple pairs. 

# In[41]:


dict = {'Name': 'Zara', 'Age': 7} 
print ("Value : %s" %  dict.items())


# In[ ]:




