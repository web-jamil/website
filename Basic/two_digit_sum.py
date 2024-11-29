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
    
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))
bmi = weight / (height ** 2)  # Use division operator and parentheses for correct precedence
bmi_as_integer = int(bmi)  # Convert BMI to an integer
print(f"Your BMI as an integer is: {bmi_as_integer}")
