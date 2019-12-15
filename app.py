# name = input("What's your name? ")
# favourite = input("What's your favourite color ")
# print(name + 'Likes' + favourite)


# weight = int(input("Enter your weigth "))
# kg = weight * 0.45359237
# print(kg)


# x = 2.9
# print(abs(x))
# print(round(x))


#today task

#if else conditions
# hot = True
# cold=True
# if hot:
#     print("It's hot day")
#     print("Drink plenty of water")
# elif:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
# print("It's a lovely day")

#Buying a house
# price = 1000000
# credits = True
# if credits:
#  payment = 0.1 * price
# else:
#     payment = 0.2 * price
#     print(f"payment: ${payment}")

#Tells the temperature wheather its hot or not
# temperature = 35
# if temperature > 30:
#     print("Temperature is hot")
# else:
#     print("Temperature isn't hot")

#limit
# name ="Saad"
#
# if len(name) < 3:
#     print("It must be at least 3 character")
# elif len(name) >50:
#     print("Name must be 50 character")
# else:
#     print("Name looks Good")

#Weight coverter
# weight = int(input("Weight: "))
# convert = input("(L)bs or (K)gs: ")
# if convert.upper() == "L":
#    con = weight*0.45
#    print(f"You are: {con} kilogram")
# else:
#     con = weight/0.45
#     print(f"You are {con} pounds")

#Guessing Number Game
# Snumber =9
# i = 0
# limit =3
# while i < limit:
#     guess = int(input("Guess the Secret number: "))
#     i += 1
#     if guess == Snumber:
#         print("You Won :D")
#         break
# else:
#     print("You failed to guess :P")

#Nested Loop
# number = [5, 2,  5, 2, 2]
# for i in number:
#     output = ''
#     for n in range(i):
#         output += '*'
#     print(output)

#Large number

num = [300 , 500  ,700 ,100]
max=num[0]
for i in num:
    if i> max:
        max= i
print(max)
