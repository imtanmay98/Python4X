# lets say we want to get the name of the user who is using our app
# Thisis wherewe get user input
#python gives us inbuilt input function to read the user input from from keyboard
"""
syntax:
input()
"""
#Ex,
username= input("please enter your name ")
age = input("please enter your age ")
print(username)
print(type(username))
print(age)
print(type(age))

# input() will always accepts the value as string
# so to overcome this limitation we use int(), float(), bool(), complex() etc
#Ex,

age1 = int(input("please enter your age "))
print(age1)
print(type(age1))









