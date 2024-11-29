# # # # python strings 
# # # # strings is sequences of unicode characters .we can use single or double quotes to represent strings.Multiline strings can be denoted by using triple quotes ''' or """.

# # # # Example:can't write string with out quotes either single ,double or triple quotes
# # # #just like a list and tuple the slicing operator can be used wit hstrings .however strings are immutable .so we can not change the original string .we can only make a new string.
# # # s="hello world"
# # # print(s[0]) #prints h
# # # print("s[4]=" ,s[4]) #prints o
# # # print("s[6:11]=",s[6:11]) # world
# # # print("s[0:6] =",s[0:6]) #prints world

# # # # python set{}
# # # # set is an unordered collection of unique items.set is defined by values separated by comma inside braces{}.items in a set are not ordered.
# # # a={1,"apple",2,"banana",3,"cherry"}
# # # print("a=",a)
# # # print(type(a)) #<class 'set'>
# # # # since set are unordered ,indexing has no meaning .hence the slicing operator[] has no use in set.
# # # """ dictionary is an unordered collection of key-value pairs . it is generally used when we have a huge amount of data .dictionaries are optimized for retrieving data .we must know the key to retrieve the value.we must know the key to retrieve the value.in python ,dictionaries are defined within braces{} with each item being a pair in the form key:value .key and value can be of any type.it can be accessed using the key """
# # # f={1:"apple",2:"banana",3:"cherry"}
# # # print(f,type(f))
# # # print(f[3])
# # # f[1]="mango"
# # # print("f[1]=",f[1])
# # # print("d['key']=",f[1])
# # # print(zip([1,2,3],['apple','banana','cherry']))
# # # # this process doesn't need any user involvement .it is done automatically.

# # # first_name="Milaan"
# # # print(first_name)
# # # first_name_to_list=list(first_name)
# # # print(first_name_to_list)
# # # # to convert to dictionary ,each element must be a pair
# # # dict([[1,2],[3,4]])
# # # print(dict([[1,2],[3,4]])) #[[1,2],[3,4]] is tuple and now converting to a dictionary
# # # x=dict([(1,2),(3,4)]) #[(1,2),(3,4)] is tuple and now converting to a dictionary
# # # print(x)
# # a=9
# # print("The value of a is:",a)
# # # syntax of print() function is print(value(s),sep=separator,end=end, file=file,flush=flush)

# # # print(*objects,sep="",end="\n",file=sys.stdout,flush=False)  #the sep separator is used between the values . it defaults into a space character. after all values are printed ,end is printed .it defaults into a new line.
# # # after all values are printed ,end is printed .it defaults into a new line.
# # # syntax input([prompt])  #prompt is a string that is written to standard output without a trailing newline. the function then reads a line from input ,converts it to a string (stripping a trailing newline), and returns that.
# # """ input([prompt])
# # # input([prompt])-->prompts for and returns input as a string  
# name,age,phone=input("Enter your name,age,phone number:").split()
# print("\n")
# print("User Details :",name,age,phone)
# print(type(phone))

