# from string import Template

# template = Template("Name: $name, Age: $age")
# output = template.substitute(name="Alice", age=25)
# print(output)
# # Output: Name: Alice, Age: 25


# from string import Template
# template = Template("Name: $name, Age: $age")
# output=template.substitute(name="Alice",age=25)
# print(output)


# print("{:.2f}".format(3.14159))
# # Output: 3.14
# try:
#     print(int("hello"))
# except ValueError:
#     print("Invalid conversion!")

# def hello_world():
#     print("Hello, World!")
# hello_world()

# print("Hello " +input("what is you name"))
# str.lower():-> converts all characters to lower case 
# str.upper():-> converts all characters to upper case

# string="HELLO".lower()
# print(string)

# str.upper()-> converts all characters to uppercase 

# str.capitalize()->converts all first characters to uppercase and rest to lowercase


# str.title():converts the first character of each word to uppercase 

# print(len(input("what is your name? ")))

# first_name = 'Milaan'
# last_name = 'Parmar'
# country = 'Finland'
# city = 'Tampere'
# age = 96
# is_married = True
# skills = ['Python', 'Matlab', 'JS', 'C', 'C++']
# person_info = {
#    'firstname':'Milaan',
#    'lastname':'Parmar',
#    'country':'Finland',
#    'city':'Tampere'
#     }

# print(type(person_info))


# # Example:

# fruits1 = ('''Banana''', "Apple", "Strawberry")             # tuple ()
# fruits2 = ["Banana", "Apple", "Strawberry"]             # list []
# fruits3 = {"Banana", "Apple", "Strawberry"}             # set {}
# fruits4 = {"1":"Banana", "2":"Apple", "3":"Strawberry"} # dictionary {"Key":"Value"}

# print(fruits1)
# print(fruits2)
# print(fruits3)
# print(fruits4)


# fruits = ["apple", "mango", "orange"] #list
# numbers = (1, 2, 3) #tuple
# alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
# vowels = {'a', 'e', 'i' , 'o', 'u'} #set

# print(fruits)
# print(numbers)
# print(alphabets)
# print(vowels)

# old_list=[[1,2,3],[4,5,6],[7,8,9]]
# new_list=old_list
# new_list[2][2]=18
# print("Old list:",old_list)
# print("New list:",new_list)

# import copy 
# x=[[1,2,3],[4,5,6],[7,8,9]]
# copy.copy(x)
# print(x)
# x.append([10,11,12])
# copy.deepcopy(x)
# print(x)

# n_list=["happy",[2,3,4],[5,6,7]]
# print(n_list[0][1])
list=['foo','bar','baz','qux','quux','corge']
print(list[1:4])
print(list[0:])
print(list[:4])
print(list[:])
print(list[-4:-1])
print(list[-1: :-1])
print(list[-1: :-2])
print(list[::2])
print(len(list)-1)
does_exist='foo' in list
print(does_exist)