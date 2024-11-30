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

