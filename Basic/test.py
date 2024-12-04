#filter even numbers from a list 
# nums=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x:x%2==0,nums))
# print(even)
# from functools import reduce
# nums=[1,2,3,4,5,6,7,8,9,10]
# product=reduce(lambda x,y:x*y,nums)
# print(product)

# add=lambda x,y=5:x+y
# print(add(3))
# print(add(3,10))


# nums=[1,2,3,4,5,6,7,8,9,10]
# square=[(lambda x:x**2) (x) for x in nums]
# print(square)
# def is_even(x):
#   return x%2==0
# evens=list(filter(is_even,range(10)))
# print(evens)
# reverse_string=lambda x:x[::-1]
# print(reverse_string("hello"))
# print(reverse_string("python"))
# print(reverse_string("world"))
# print(reverse_string("programming"))

# result=[x for x in range(10) if x%2==0]
# print(result)
# result=[x*2 for x in range(10)]
# print(result)
# format_string=lambda first,last:f"Name :{first} {last}"
# print(format_string("John","Doe"))

formatter=lambda name,age:f"My name is {name} and I am {age} Years old.you live longer than you think {name}"
print(formatter("Alice",25))