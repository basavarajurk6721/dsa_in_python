# my_list = [1, 2, 3, 4, 5]
# myVal = my_list[0]

# for i in my_list:
#     if i < myVal:
#         myVal = i

# print("The minimum value in the list is:", myVal)

# my_set = {1, 2, 3, 4, 5}
# vinu_set ={4, 5, 8, 9, 10}
# v = my_set.intersection(vinu_set)
# print("The set is:", my_set)
# print("The intersection is:", v)

# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x == y)
# print(x is x)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango" ,"banana"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# thislist.remove("banana")
# for x in range(len(thislist)):
#     print(thislist[x])
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i+=1
# print(thislist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist=[]
# # for x in fruits:
# #     if 'a' in x:
# #         newlist.append(x)
# b = fruits.sort()
# print(b)

# thislist = ["Orange", "Mango", "Kiwi", "Pineapple", "banana"]
# # thislist = [50 ,89 ,1 ,3, 5]
# thislist.reverse()
# print(thislist)

# def myfunc(n):
#     return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)
# print("banana" in thisset)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3 ,"a" ,"b"}
# set3 = set1.symmetric_difference_update(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# 31
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2) 
# print(set1)


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["color"] = "red"
# print(x) 

# thisdict = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# thisdict = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# day = 4
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Today is a weekday")
#     case 6 | 7:
#         print("I love weekends!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)

# def my_function(fname):
#     print(fname + " Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname, lname):
#     print(fname + " " + lname)
# my_function("Emil", "Refsnes")

# def my_function(name = "friend"):
#     print("Hello", name)
# my_function("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")

# def my_function(animal, name):
#     print("I have a", animal)
#     print("My", animal + "'s name is", name)
# my_function(name = "Buddy", animal = "dog")

# def my_function(animal, name, age):
#     print("I have a", age, "year old", animal, "named", name)
# my_function("dog", name = "Buddy", age = 5)

# def my_function(*kids):
#     print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")

# def my_function(greeting, *names):
#     print(greeting)
#     for name in names:
#         print(name)

# my_function("Hello", "Emil", "Tobias", "Linus")


# def my_function(*numbers):
#     """Returns the maximum number from a list of numbers."""
#     if len(numbers) == 0:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
# print(my_function(3, 7, 2, 9, 1))


# def my_function(**kid):
#     print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(username, **details):
#     print("Username:", username)
#     print("Additional details:")
#     for key, value in details.items():
#         print(" ", key + ":", value)

# my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# def my_function(title, *args, **kwargs):
#     print("Title:", title)
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# x = 300
# def myfunc():
#     global x
#     x = 200
# myfunc()
# print(x)

# def myfunc1():
#     x = "Jane"
#     def myfunc2():
#         nonlocal x
#         x = "hello"
    
#     myfunc2()   
#     return x
# print(myfunc1())

# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello Sally"

# @changecase
# def otherfunction():
#     return "I am speed!"

# print(myfunction())
# print(otherfunction())


# def changecase(n):
#     def changecase(func):
#         def myinner():
#             nonlocal n
#             if n == 1:
#                 a = func().lower()
#             else:
#                 a = func().upper()
#             return a
#         return myinner
#     return changecase
# @changecase(2)
# def myfunction():
#     return "Hello Linus"
# print(myfunction())

# def myfunc(n):
#     return lambda a : a * n
# mydoubler = myfunc(6)
# print(mydoubler(11))

# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)

# words = ["apple", "pie", "banana", "cherry"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)

# def countdown(n):
#     if n<=0:
#         print("done")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(1))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(7))


# def my_generator():
#     print("First")
#     yield 10

#     print("Second")
#     yield 20

#     print("Third")
#     yield 30

# g = my_generator()

# for value in g:
#     print(value)

# print(next(g))
# # print(next(g))
# print(next(g))

# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# for num in count_up_to(5):
#     print(num)

# total = sum(x * x for x in range(10))
# print(total)

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b # Get first 100 Fibonacci numbers
# gen = fibonacci()
# for _ in range(100):
#     print(next(gen))

# def counter():
#     try:
#         x = yield 1
#         print("Received:", x)
#         yield 2
#         yield 3
#     finally:
#         print("Generator cleanup")

# g = counter()

# print(next(g))
# print(g.send(100))


# mystr = "banana"
# myit = iter(mystr)
# for x in myit:
#     print(x)

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myclass = MyNumbers()
# myiter = iter(myclass)

# for num in myiter:
#     print(num)

# import datetime
# x = datetime.datetime.now()
# print(x)

# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))



# try:
#     x = int(input("Enter a number: "))
#     if x < 0:
#         raise ValueError("Negative value entered")
#     print("You entered:", x)
# except ValueError as ve:
#     print("ValueError:", ve)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")