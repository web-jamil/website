# def sum_of_two_digits(number):
#     if 10 <= number <= 99:  # Ensure the number is a two-digit number
#         tens = number // 10  # Get the tens digit
#         ones = number % 10   # Get the ones digit
#         return tens + ones
#     else:
#         raise ValueError("Input must be a two-digit number.")

# # Example usage:
# try:
#     number = int(input("Enter a two-digit number: "))
#     result = sum_of_two_digits(number)
#     print(f"The sum of the digits is: {result}")
# except ValueError as e:
#     print(e)
    
# height = float(input("Please enter your height in meters: "))
# weight = float(input("Please enter your weight in kilograms: "))
# bmi = weight / (height ** 2)  # Use division operator and parentheses for correct precedence
# bmi_as_integer = int(bmi)  # Convert BMI to an integer
# print(f"Your BMI as an integer is: {bmi_as_integer}")

# age=int(input('enter your age:'))
# year_left=90-age
# days_left_of_year=year_left*365
# weeks_left_of_year=year_left*52
# months_left_of_year=year_left*12
# print(f'You have {days_left_of_year} days, {weeks_left_of_year} weeks, and {months_left_of_year} months left.')


# print("welcome to the tip calculator")
# total_bill=float(input("What was the total bill? $"))
# percentage=int(input("What percentage would you like to give as a tip? "))
# people=int(input("How many people to split the bill? "))
# tip=total_bill*(percentage/100)
# total_bill_with_tip=total_bill+tip
# bill_per_person=total_bill_with_tip/people
# final_amount=round(bill_per_person,2)
# final_amount="{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")


# print("welcome to the even or odd number checker")
# enter_number=int(input("Enter a number: "))
# if enter_number%2==0:
#   print("this is an even number")
# else:
#   print("this is an odd number")
  
# height = float(input("enter your height in cm: "))
# if height>=120:
#   print("you can ride the rollercoaster")
#   age=int(input("enter your age: "))
#   if age<12:
#     print("please pay $5")
#   elif age<=18:
#     print("please pay $7")
#   else:
#     print("please pay $12")
# else:
#   print("you cannot ride the roller")
  
# c=6+3j
# print(c.real)
# print(c.imag)
# print(c.conjugate())
# print(c+3)
# print(isinstance(c,complex))

# print(0b0001)
# print(0x000A)"window.menuBarVisibility": "classic"




""" in python the capitalize method converts first character of a string to uppercase and all other characters to lowercase.if any
syntax:
 string.capitalize()
 capitalize parameters 
 the capitalize() method doesn't take any parameters.
 return value from capitalize()
 the capitalize() function return a string with the first character in uppercase and all other characters in lowercase.
 it doesn't modify the original string.

"""
# string="+ hello, and welcome to my world."
# capitalized_string=string.capitalize()
# print("old string:",string)
# print("new string:",capitalized_string)
""" 

python string center()
the center() method returns a string which is padded with the specified character
syntax:
  string.center(width[,fillchar])
  the center() method takes two arguments:
    width: length of the string  with padded character 
    fillchar(optional): padding character. 
    the fillchar argument is optional .if it's not provided ,space is taken as default value"""
    
""" RETURN value from center()
    the center() method returns a string padded with specified fillchar.it doesn't modify the original string."""

# string="Python is awesome"
# new_string=string.center(44,'*')
# print("centered string:",new_string)
# print("original string:",string)


# python list method
""" python list index() methods return the index of the specified element in the list.
syntax:
list.index(element,start,end)
the list index() method can take a maximum of three arguments:
element-the element to be searched 
start(optional) :start searching from this index
end(optional):search the element up to this index

the index() method returns the index of the given element in the list .if the element is not found,a valueError exception is raised.
the index() method only returns the first occurrence of the matching element.
"""
# vowel=['a','e','i','o','u']
# index=vowel.index('e')
# print('the index of e:',index)
# index=vowel.index('i',2,4)
# print('the index of i:',index)

""" 
python list append() methods 
the append() method adds an item to the end of the list .
syntax:
list.append(item)
append() parameters
the append() methods take a single argument.
 1.item-the item to be added at the end to the list
 2.the items can be numbers ,strings,dictionaries,another list and so on.
the append() method doesn't return any value;it returns None.

"""

# animals=['cat','dog','rabbit']
# animals.append('guinea pig')
# print(animals)  # ['cat', 'dog', 'rabbit', 'guinea pig']
# animals=['cat','dog','rabbit']
# wild_animals=['tiger','fox']
# animals.append(wild_animals)
# print('updated animals list:',animals)

""" the extend() method adds all the elements of an iterable(list,tuple,string etc) to the end of the list.
syntax:
list.extend(iterable)
the extend() method take an iterable such as list,tuple,string etc.
the extend() method modifies the original list.it doesn't return any value.
# """
# languages=['french','english','german']
# languages1=['spanish','portuguese']
# languages.extend(languages1)
# print('languages list:',languages)
# print('languages1 list:',languages1) 


languages=['french','english','german']
language_tuple=('spanish','portuguese')
languages.extend(language_tuple)
languages_set={'chinese','japanese'}
languages.extend(languages_set)
print('updated languages list:',languages)

""" OTHER WAYS  TO EXTEND A LIST   
you can also append all elements of an iterable to the list using the += operator.



"""
# a=[1,2]
# b=[3,4]
# a+=b
# print('a:',a)
# the slicing SyntaxError
# a=[1,2]
# b=[3,4]
# a[len(a):]=b
# print('a:',a)

# if you need to add an element to the end of a list ,you can use the append() method.
a1=[1,2]
a2=[1,2]
b=(3,4)
a1.extend(b)
print(a1)

a2.append(b)
print(a2)
""" the list insert() method inserts an element to the list at the specified index 
syntax
list.insert(i,elem)
here , elem is inserted to the list at the ith index.all the elements after elem are shifted to the right
insert() parameters
the insert() methods takes two parameters
index-the index where the elements needs to be inserted 
element-this is the element to be inserted in the list f
notes:
1.if index is 0,the element is inserted at the begining of the list 
2.if index is 3,the element is inserted after the 3rd element in the list 
3.if index is -1 ,the element is inserted after the last element in the list
4.if index is -3,the element is inserted after the 3rd element from the end of the list
the insert() method doesn't return anything returns none .it only updates the current list.
"""
# vowel=['a','e','i','u']
# vowel.insert(-3,'o')
# print('updated list:',vowel)

# mixed_list=[1,2,3,'example',3.132,{1:'one',2:'two',3:'three'},(1,2,3),{1,2,3}]
# number_tuple=(4,5,6)
# mixed_list.insert(1,number_tuple)
# print('updated list:',mixed_list)

""" the list remove() method removes the first matching element (which is passed as an argument) from the list .
syntax:
list.remove(element)
remove() parameters
the remove() method takes a single element as an argument and removes it from the list
if the element doesn't exist ,it throws value Error :list.remove(x):x not in list exception

the remove() method doesn't return  any value (return none)

"""
# animals=['cat','dog','rabbit','guinea pig']
# animals.remove('rabbit')
# print('updated animals list:',animals)

# animals=['cat','dog','rabbit','guinea pig','rabbit']
# animals.remove('rabbit')
# print('updated animals list:',animals) # throws value error :list.remove(x):x not
# animals=['cat','dog','rabbit','guinea pig']#
# animals.remove('lion')
# print('updated animals list:',animals) # throws value error :list.remove(x):x not


""" the python list count() method returns the number of times the specified element appears in the list.

syntax:
list.count(element)

count() parameters 
the list count() method takes a single argument '
element-the element to be counted in the list
the count methods returns the number of times the specified element appers in the list



"""

# vowels=['a','e','i','o','i','u']
# count=vowels.count('i')
# print('the count of i is:',count)
# count=vowels.count('p')
# print('the count of p is:',count) # returns 0 because p is not in the list
# random=['a',('a',1),1,2,3];
# count=random.count(('a',1))
# print('the count of (a,1) is:',count) # returns 1 because 
""" the pop() methods removes the item at given index from the list and return the removed item """

""" the pop() method removes the item at the given index from the list and returns the removed item 
syntax:
list.pop(index)

pop() parameters
1.the pop() method takes a single argument(index)
2.the argument passed to the method is optional.if not passed ,the default index -1 is passed as an argument(which means the last item will be removed a)
3.if the index passed to the method is not in range ,it throws IndexError:pop index out of range exception

return value from pop()
the pop() method return the item present at the given index .this item is also removed from the list 
"""

# languages=['python','java','c++','french','c']
# return_value=languages.pop(3)
# print('return value:',return_value)
# print('updated list:',languages)
# note : index in python starts from 0 not 1

""" 
the reverse() methods reverses the elements of a given list.
syntax:
list.reverse()
reverse() parameters
the reverse() method doesn't take any arguments
return value from reverse( )
the reverse() method doesn't return any value.it updates the existing list.
"""
# systems=['windows','macos','linux']
# print('original list:',systems)
# systems.reverse()
# print('updated list:',systems)

# systems=['windows','macos','linux']
# print('original list:',systems)
# reversed_list=systems[::-1] # reversed_list=systems[start:stop:step]
# print('updated list:',reversed_list)

# systems=['windows','macos','linux']
# for o in systems:
#   print(o)

""" python sort() method sorts the elements of a given list in a specific ascending or descending order.
syntax:
list.sort(key=none,reverse=false)
alternatively you can also use python built's in sorted function for the same purpose.
sorted(list,key=none,reverse=false)
notes:

the simplest difference between sort() and sorted() is : sort() changes the list directly and doesn't return any value ,while sorted() doesn't change the list and returns the sorted list. 

by default ,sort() doesn't require any extra parameters however, it has two optional parameters
reverse-if true ,the sorted list is reversed (or sorted in descending order)
key- function that serves as a key for the sort comparison
return value from sort()
the sort() method doesn't return any value ,rather it changes the original list.

"""
vowels=['e','a','u','o','i']
vowels.sort()
print('sorted list:',vowels)


""" sort in descending order 
THE sort method accepts a reverse parameter as an optional argument.
settings reverse=True sorts the list in the descending order
alternatively for sorted() you can use the following code
sorted(list,reverse=True)

python list copy() 
the copy() method returns a shallow copy of the list.
a list can be copied  using the = operator.
syntax:
new_list=list.copy()
copy() parameters
the copy() method doesn't take any parameters

the copy() method returns a new list.it doesn't modify the original list.

"""
# old_list=[1,2,3]
# new_list=old_list
# new_list.append('a')
# print("new list:",new_list)
# print("old list:",old_list)


# my_list=[1,2,3]
# new_list=my_list.copy()
# new_list.append('a')
# print('new list:',new_list)
# print('my list:',my_list)

# copy list using slicing syntax
# list=[1,2,3]
# new_list=list[:]
# new_list.append('a')
# print('new list:',new_list)
# print('my list:',list)

""" PYTHON LIST clear() method
the clear() method removes all items from the list.
syntax:
list.clear()
pop() parameters
the clear() method doesn't take any parameters
return value from clear()
the clear() method only empties the given list. it doesn't return any value.

"""

# working with clear method
# list=[(1,2),('a','b'),{'A':1,'B':2},[1,2]]
# list.clear()
# print('list:',list)

list=[{1,2},('a','b'),[1,2]]  # list of sets,tuples and list
del list[:]
print('list:',list)