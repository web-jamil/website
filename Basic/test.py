# x = 5

# # Checks if x is not less than 10
# if not x < 10:
#     print("x is not less than 10.")  # Output: x is not less than 10.
# else:
#     print("x is less than 10.")
# person = {"name": "Alice", "age": 30, "city": "New York"}
# for key in person:
#     print(f"{key} : {person[key]}")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
country=["USA","UK","India"]
for name, age,country in zip(names, ages,country):
    print(name, age,country)
