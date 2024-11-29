# python keyword are the reverse word use by python .we can't use then as a variable name or any other identifier name 
import keyword  as kw
print(kw.kwlist)
""" 
 None is a speacial constants  in python that represent the absence of a value or a null value.
 it is an objects of its own datatype .we can't create multiple None objects but can assign it to variable. these variables will be equal to one another.
 we must take care  none that does not imply False, 0 or any empty list,dictionary,string etc.
 
 
 """
def improper_return_function(a):
   if(a%2) ==0:
     return True
x=improper_return_function(3)
print(x)

""" void functions that do not return anything will return a None Object automatically .None is also returned by functions in which the program flow does not encounter a return statement.

"""
""" _peg_parser_
the _peg_parser_ keyword is new keyword in python .the _new_parser_ was renamed to _peg_parser_ recently in python  3.9.
and will results true if both the operands are true. or will result into true if any of the two operands is true.
not operator is used to invert the truth value. the not operator invert the false value """
""" 
as is used to create an alias while importing a module .it means giving a different name to a module while importing it .
 """
""" import math as myAlias
print(myAlias.sqrt(25))
assert is used for debugging  purposes.
while programmingsometimes we wish to know the internal state or check if our assumptions are true .assert helps us do this and finds bugs more conveniently .assert is followed by a condition. """
""" a=4
assert a>5
assert a<4
break and continue are used inside for and while loops to alter their normal behavior.

 """
for i in range(1,11):
   if i==5 :
     break
   print(i)   #function is a block of  related code ,which together does a specific task it helps us to organize code into manageable chunks and also to do some repetitive task.
   
   
""" def function_name(parameters):
  #function body
  #return value
# function is a block of related code ,which together does a specific task .it helps us to organize code into manageable chunks and  also to do some repetitive task 
# del is used to delete the reference to an objects . everything is object in python and we can delete a reference to an object using del keyword.
"""
a=['x','y','z']
del a[1]
print(a)
# python keyword are the reverse word use by python .we can't use then as a variable name or any other identifier name 
import keyword  as kw
print(kw.kwlist)
""" 
 None is a speacial constants  in python that represent the absence of a value or a null value.
 it is an objects of its own datatype .we can't create multiple None objects but can assign it to variable. these variables will be equal to one another.
 we must take care  none that does not imply False, 0 or any empty list,dictionary,string etc.
 
 
 """
def improper_return_function(a):
   if(a%2) ==0:
     return True
x=improper_return_function(3)
print(x)

""" void functions that do not return anything will return a None Object automatically .None is also returned by functions in which the program flow does not encounter a return statement.

"""
""" _peg_parser_
the _peg_parser_ keyword is new keyword in python .the _new_parser_ was renamed to _peg_parser_ recently in python  3.9.
and will results true if both the operands are true. or will result into true if any of the two operands is true.
not operator is used to invert the truth value. the not operator invert the false value """
""" 
as is used to create an alias while importing a module .it means giving a different name to a module while importing it .
 """
""" import math as myAlias
print(myAlias.sqrt(25))
assert is used for debugging  purposes.
while programmingsometimes we wish to know the internal state or check if our assumptions are true .assert helps us do this and finds bugs more conveniently .assert is followed by a condition. """
""" a=4
assert a>5
assert a<4
break and continue are used inside for and while loops to alter their normal behavior.

 """
for i in range(1,11):
   if i==5 :
     break
   print(i)   #function is a block of  related code ,which together does a specific task it helps us to organize code into manageable chunks and also to do some repetitive task.
   
   
""" def function_name(parameters):
  #function body
  #return value
# function is a block of related code ,which together does a specific task .it helps us to organize code into manageable chunks and  also to do some repetitive task 
# del is used to delete the reference to an objects . everything is object in python and we can delete a reference to an object using del keyword.
"""
a=['x','y','z']
del a[1]
print(a)

#del is also used to delete items from a list or a dictionary.
# if ,else  ,elif ae used for conditional branching or decision making 
# def if_example(a):
#   if a==1:
#     print('one')
#   elif a==2:
#     print('two')
#   else:
#     print('something else')
# if_example(2)
# if_example(4)
""" 
def reciprocal(num):
  try:
    r=1/num
  except:
    print('exception caught')
    return
  return r
print(reciprocal(10))
print(reciprocal(0))  #try and except are used to handle exceptions or errors in

for is used for looping .generally we use for when we know the number of times we want to loop .

 """""" 
names=['jhon','Monica','Steven','Robin']
for i in names:
  print('Hello '+i)
  
a = ['x', 'y', 'z']
if 'x' in a:
    print('found')
in is used to test if a sequence (list ,tuple,string etc) contains a value .it return true if the value is present ,else it returns false. """

for i in "hello":
  print(i) 
  
  
num_char=len(input('enter your name:'))
print('your name has '+str(num_char)+' characters')