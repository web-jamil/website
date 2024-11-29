# # # """ strings in python are sequences of characters enclosed in quotes:
# # #   1.by using singles quotes.
# # #   3.by using double quotes.
# # #   2.by using triple quotes(for multi-line strings ) """
# # # single_quote='Hello'
# # # double_quote="World"
# # # triple_quote='''This is a multi 
# # # line string'''
# # # print(triple_quote)
# # # print(single_quote)
# # # print(double_quote)
# # # # using str() to convert other types
# # # #using raw strings (ignoring escape characters)

# # # raw=r"This is a raw string with backslash :\\ "
# # # print(raw);
# # # triple_quotes="""This is a Multi_line strings double quotes """;
# # # print(triple_quote)

# # # s="hello" +" "+"world"
# # # print(s)
# # # #repeat strings using *
# # # s="Hello "*3;
# # # print(s)
# # # # using the + operator to concatenate strings
# # # str1="Jamil"
# # # str2="is Coding"
# # # result=str1+" "+str2
# # # print(result) 

# # words=["python","is","fun"]
# # result=" ".join(words)
# # print(result)

# # fruits=["apple","banana","cherry"]
# # result=",".join(fruits)
# # print(fruits)


# # tuple_data=("one","two","three")
# # result=" ".join(tuple_data)
# # print(result)  # Output: onetwothree

# # # joining characters
# # chars=['H','e','l','l','o'];
# # result="".join(chars);
# # print(result)  # Output: Hello

# # # non-string elements: if the iterable contains non-string elements, a typeerror occurs
# # # to fix this ,converts elements to strings first
# # # using map() function to convert elements to strings
# # data=["Hello",123,"World"]
# # result=" ".join(map(str,data))
# # print(result)  # Output: Hello 123 World

# # # joining generator expressions 
# # squares=(str(x*2) for x in range(5))
# # result=",".join(squares)

# # # joining with empty separator
# # numbers=["1","2","3"]
# # result="-".join(numbers)
# # # print(result) if you have nested iterables ,you need to flatten them or process them first 
# # # nested=[["a","b"],["c","d"]] immutable separator : the join method does not modify the separator or the original iterable
# # # the join method is more-efficient than concatenating strings in a loop,as it avoids creating intermediate strings.
# # result="".join("".join(inner) for inner in nested)
# # print(result)
# # jamil=[["jamil","is","coding","."],["jamil","is","web developer"]]
# # resultjamil=' '.join(' '.join(inner) for inner in jamil)
# # print(resultjamil)  # Output: jamilis coding jamilis web developer

# # using the interpolation (f-strings)--> introduced in python 3.6 ,f-strings allow embedding expressions inside string literals

# name="Alice "
# greeting=f"Hello,{name}"
# print(greeting)  # Output: Hello,Alice
# greeting="Hello,%s" %name
# print(greeting)  # Output: Hello,Alice
# greeting="Hello , {}!".format(name)
# print(greeting)  # Output: Hello , Alice!

# # you can repeat strings by multiplying them with an integer
# result=name*3
# print(result)  # Output: wordwordword

# ''' use  + for simplicity when concatenating a small number of strings'''
# '''use join() for concatenating large number of strings for better performance '''
# '''prefer f strings for readability and embedding variable or expressions'''

# #string formatting in python allows you to dynamically construct strings by embedding variables or expressions in a string template

# #using f -strings(recommended )
# # #introduced in python 3.6 ,f-strings allow embedding expression inside curly braces {}
# # name="jamil"
# # last_name="uddin"
# # age=25
# # coding_profile="contest programmer using leetcode for the contest "
# # greeting=f"Hello , my name is {name} {last_name} , i am {age} years old And  i am {coding_profile}"
# # print(greeting)

# # arithmetic operations on strings
# # price=49.9
# # tax=0.05
# # print(f"Total : {price+price*tax:.2f}")

# # def greet(name):
# #   return f"Hello , {name}"
# # print(greet("jamil"))  # Output: Hello , jamil
# # # indexing and slicing 
# # fruits=["apple","banana","cherry"]
# # print(f"My favorite fruit is {fruits[0]}")

# #formatting options
# # 1.Number formatting
# num=123.456
# print(f"{num:.2f}")
# # 2.thousand separator
# num=1234567
# print(f"{num:,}")

# path="c:\\users\\Admin"
# print(fr"Path:{path}")
# name="Alice"
# print(rf"Hello, { name} \n How are you?")  # Output: Hello, Alice
# value=42.0089
# print(rf"{{value is {value:.3f}}}")


# in python comments are used to document the code and make it more understandable .comments are  ignored by the python interpreter ,so they do not affect how the code runs 

# there are two types of comments in python 
# 1.single line comments 
""" use the # symbol for single line comments and everything after the # on that kine is treated as a comment and ignored by the python interpreter """

#This is a single line comment 
print("Hello,World") #This is an inline comment
# 2.multi line comments`
# """ python doesn't have specific syntax for multi-line comments like other programming languages but you can use either """
#1. Multiline # lines : add a# at the beginning of each line to make it a multiline comment 
#This is a multiline comment 
#each line starts with a hash 
#python ignore all of them

# using triples quotes (''') or("""):triples quotes are generally used for docstrings  but can serve as mutliline comments if not assigned to a variable or used as a function description
'''This is a multiline comments
spanning multiple lines 
using the triple singles quotes '''

"""Alternatively ,you can use triple double quotes as well"""
# 3. Docstrings( short for documentation strings ) are special type of command used to document functions, classes or modules .they are enclosed in triple quotes and can span multiple lines
# unlike regular comments ,docstrings are accessible via the _doc_ atrribute

def my_function():
  '''This is a docstrings for the function
  .It explains what the function does .'''
print(my_function.__doc__)

# use single line comments for short ,explanatory notes
# docstrings vs comments 
# 1. regular comments are ignored by the intepreter
# 2.docstrings (''') or (""") are not ignored by the interpreter and can be accessed via the _doc_ attribute, are stored as  metadata for the function ,class or module and can be accessed programmatically 
# python doesn't support nested comments . if you need to disable a block of code use multiple # lines or a code editor's commenting tool
