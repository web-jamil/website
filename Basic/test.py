# import copy

# original = [1, 2, [3, 4]]
# shallow_copy = copy.copy(original)

# # Modify the inner list in the copy
# shallow_copy[2].append(5)

# print("Original:", original)        # Output: [1, 2, [3, 4, 5]]
# print("Shallow Copy:", shallow_copy) # Output: [1, 2, [3, 4, 5]]
# import copy

# original = [1, 2, [3, 4]]
# deep_copy = copy.deepcopy(original)

# # Modify the inner list in the copy
# deep_copy[2].append(5)

# print("Original:", original)     # Output: [1, 2, [3, 4]]
# print("Deep Copy:", deep_copy)   # Output: [1, 2, [3, 4, 5]]


""" 
python  dictionary get ()
the get() method returns the value for the specified key if key is in dictionary
syntax:
dict.get(key[,value])
get() parameters 

the get() method takes maximum of two parameters:
key-key to be searched in the dictionary
value(optiona)-value to be returned if the key is not found the default value is None.



return value from get()
the get() method returns:
1.the value for the specified key if key is in dictionary
2.None if the key is not found and value is not specified
3.value if the key is not found and value is specified

"""

# person={"name":"Phill","age":22}
# print("Name:",person.get("name"))
# print("Age:",person.get("age"))
# print("Salary:",person.get("salary"))
# print("Salary:",person.get("salary",0.0))


# person={}
# print("Salary:",person.get("salary","value is not found"))
""" 
python dictionary pop()
the pop() method removes and return an element from a dictionary 
having the given key
syntax:
dictionary.pop(key[,default]);
pop() parameters 
the pop() methods takes two parameters 
1.key-key which is to be searched for removal
2.default- value which is to be returned when the key is not in the dictionary
return value from pop()
the pop() method returns:
1.if key is found -removed/popped element from the dictionary
2.if key is not found -value specified as the second argument(default)
3.if key is not found and default argument is not specified keyError exception is raised

"""


# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
# element = sales.pop('apple')
# print(element)  # Output: 2
# print(sales)  # Output: {'orange': 3, 'grapes': 4}

#vowels keys
# keys={'a','e','i','o','u'}
# vowels=dict.fromkeys(keys)
# print(vowels)

# keys={'a','e','i','o','u'}
# value='vowel'
# vowels=dict.fromkeys(keys,value)
# print(vowels)
# vowels={'a','e','i','o','u'}
# value=[1]
# vowels=dict.fromkeys(vowels,value)
# print(vowels)
# value.append(2)
# print(vowels)

# height=float(input("Enter height in meters:"))
# weight=float(input("Enter weight in kg:"))
# bmi=round(weight/(height**2))
# if bmi<18.5:
#     print(f"Your Bmi is{bmi},you are Underweight")
# elif bmi<25:
#     print(f"Your Bmi is{bmi},you are Normal")

# elif bmi<30:
#   print(f"Your Bmi is{bmi},you are Overweight")
# elif bmi<35:
#     print(f"Your Bmi is{bmi},you are obses")
# else:
#     print(f"Your Bmi is{bmi},you are clinically obses")


"""
python dictionary update()
the update () method updates the dictionary with the elements from the another dictionary with the elements  from anopther dictionary object or from an iterable of key/value pairs
syntax:
 dict.update([other])
 update() parameters
 the update() method takes either a dictionary or an iterable object of key value pairs (generally tuples)
 if update() is called without passing parameters ,the dictionary remains unchanged.
 return value from update()
 the update () method  updates the dictionary with the elements from a  dictionary object or an iterable object of key value /pairs .
 it doesn't return any value (returns None)
"""

# d = {1: "one", 2: "three"}  # Original dictionary
# d1 = {2: "two"}  # Another dictionary
# d.update(d1)  # Update d with d1
# print(d)  # Output: {1: "one", 2: "two"}

# d1 = {3: "three"}  # New dictionary
# d.update(d1)  # Update d with d1
# print(d)  # Output: {1: "one", 2: "two", 3: "three"}
# d={1:"one",2:"three"}
# d1={2:"two"}
# d.update(d1)
# print(d)
# d1={3:"three"}
# d.update(d1)
# print(d)
# d = {'x': 2}
# d.update(y = 3, z = 0)
# print(d)

# d={"x":2}
# d.update(y=3,z=0)
# print(d)

""" 
python dictionary values()
the values() method returns a view object that displays a list of all values in a dictionary 
syntax:
 dictionary.values()
 value() parameters
 
the values() method doesn't take any parameters
return value from values()
the values() method returns a view object that displays a list of all values in a given distionary

"""

# sales={'apple':2,'orange':3,'grapes':4}
# values=sales.values()
# print("orginal items:",values)
# del[sales['apple']]
# print("updated items:",values)

""" 
syntax: 
my_dict={1:'apple',2:'ball'}

"""

# square_dict=dict()
# for num in range(1,11):
#    square_dict[num]=num*num
# print(square_dict)

# old_price={"milk":1.02,"coffee":2.5,"bread":2.5}
# dollar_to_pound=0.76
# new_price={item:value*dollar_to_pound for (item,value) in old_price.items()}
# square_dict={num:num**2for num in range(1,11)}
# print(square_dict)
# original_dict={"Alian":36, "bill":48,"cruze":30,"david":22,"elena":33,"fiora":35,"garry":37}
# even_dict={k:v for (k,v) in original_dict.items() if v%2 == 0}
# odd_dict={k:v for (k,v) in original_dict.items() if v%2 != 0}
# new_dict={k:v for (k,v) in original_dict.items() if v%2 !=0 and v<40}
# print(new_dict)
# print(odd_dict)
# print(even_dict)


# original_dict = {'Allan': 36, 'Bill': 48, 'Cory': 57, 'Dave': 33}

# # Using a single `if` condition:
# new_dict = {k: v for k, v in original_dict.items() if v % 2 != 0 if v < 40}
# print(new_dict)


# original_dict = {'Allan': 36, 'Bill': 48, 'Cory': 57, 'Dave': 33}

# Categorizing values as 'old' or 'young' based on a condition
# new_dict_1 = {k: ('old' if v > 40 else 'young') for (k, v) in original_dict.items()}
# print(new_dict_1)


# my_dict=([('name','jhon'),('age',25),('salaray',3500),('city','new York'),('country','USA'),('skills',['python','django','flask','javascript','html'])])
# print(my_dict)

# squares={x:x*x for x in range(6)}
# print(squares)

# nested_dict = {
#     'user': {
#         'name': 'Bob',
#         'age': 30,
#         'address': {
#             'city': 'Chicago',
#             'zip': '60601',
#             "country":{
#                 'country_name':'USA',
#                 'country_code':1
#             }
#         }
#     }
# }

# # Accessing nested values
# print(nested_dict['user']['address']['city'])
# print(nested_dict['user']['address']['zip'])
# print(nested_dict['user']['address']['country']['country_name'])
# # Output: Chicago



# # Basic list
# fruits = ["apple", "banana", "cherry"]

# # Empty list
# empty_list = []

# # Mixed data types
# mixed_list = [1, "hello", 3.14, True]

# # Nested list
# nested_list = [[1, 2], [3, 4], [5, 6]]

# # Using `list()` constructor
# constructed_list = list(("apple", "banana", "cherry"))  # ['apple', 'banana', 'cherry']



# my_list = [0, 1, 2, 3, 4, 5]

# # Extract a portion of the list
# print(my_list[1:4])  # Output: [1, 2, 3]

# # Omit `start` (defaults to 0)
# print(my_list[:3])  # Output: [0, 1, 2]

# # Omit `stop` (goes to the end)
# print(my_list[2:])  # Output: [2, 3, 4, 5]

# # Omit both `start` and `stop` (copy entire list)
# print(my_list[:])  # Output: [0, 1, 2, 3, 4, 5]

# even_squares=[x*x for x in range(10) if x%2==0]
# print(even_squares)

# nested_list = [[1, 2], [3, 4]]
# print(nested_list[0][1])  # Output: 2

import math
nums=[1,2,3,4,5,6,7,8,9,10]
print(sum(nums))
print(max(nums))
print(min(nums))
print(math.prod(nums))