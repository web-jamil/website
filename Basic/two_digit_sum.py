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


print("welcome to the tip calculator")
total_bill=float(input("What was the total bill? $"))
percentage=int(input("What percentage would you like to give as a tip? "))
people=int(input("How many people to split the bill? "))
tip=total_bill*(percentage/100)
total_bill_with_tip=total_bill+tip
bill_per_person=total_bill_with_tip/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")