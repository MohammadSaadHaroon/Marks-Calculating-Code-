# commands =""
# started = False
# while True:
#     commands =input("> ").lower()
#     if commands == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started")
#     elif commands=="stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started=False
#             print("Car stopped")
#     elif commands == "quit":
#         break
# else:
#     print("I dont understand")


#Today's Work 22 Nov
#list

# number =[5, 4, 3, 2, 1]
# #(Append)Insert in last
# number.append(20)
# print(number)
# #Insert in any where u want to insert
# number.insert(0, 25)
# print(number)
# #Arrange numbers in manner
# number.sort()
# print(number)
# #Remove the number whichu want to remove
# number.remove(3)
# print(number)
# #delete the last number
# number.pop()
# print(number)
# #Show the number is in that index number
# print(number.index(2))
# #Clear all th number in list
# number.clear()
# print(number)

#Exercise to remove dublicates

 # number=[2,2,4,4,9,9,10,11,13,13,15]
 # dup=[]
 # for i in number:
 #     if i  not in dup:
 #         dup.append(i)
 # print(dup)

#Tuple uses round brackets and list uses square brackets and we doesnt  append tuple

#Dictonary
# phone = input("Phone Number")
# mapping = {
#     0:"zero",
#     1:"one",
#     2:"two",
#     3:"three",
#     4:"four",
#     5:"five",
#     6:"six",
#     7:"seven",
#     8:"eight"
# }
# output = ""
# for ch in phone:
#     output += mapping.get(ch, "!") + " "
#     print(output)


#define
# def user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}')
#     print("Welcome Abroad")
#
#
# print("Start")
# #keyword arguments
# user("john", "smith")
# print("Finish")

#try n except
# try:
#     age = int(input("Age: "))
#     income = 2000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("Age cant be zero")
# except ValueError:
#     print("Invalid Value")

#Class
# class Point:
#     #constructor
#     def __init__(self, x , y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# #creating an object of class
# points = Point(10, 20)
# print(points.x)
# #Constructor is a function that get called at the time of creating object


#Excersice
# class Person:
#     def __init__(self, name):
#         self.name= name
#
#     def talk(self):
#         print(f"Hi i'm {self.name}")
#
# jo =Person("M.Saad")
# print(jo.name)
# jo.talk()

#Inheritence

# class Mammal:
#     def walk(self):
#         print("walk")
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
# class Cat(Mammal):
#     def annoying(self):
#         print("Annoying")
#
# dog1 = Dog()
# dog1.walk()
#
# cat1=Cat()
# cat1.annoying()

#Modules
# import covertors
# from covertors import lbstokgs
# lbstokgs(100)
# print(covertors.kgstolbs(70))

#Excersice
# from util import find
# num = [300 , 500  ,700 ,100]
# max= find(num)
# print(max)