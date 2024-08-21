#These aare the following contional statements
"""
1. If
2. If-else
3. If-elif-else
4. Nested if-else
"""
# If statement
"""
* It is used to check whether the particular statement  is True or False.
* If the condition is true then it will execute the statement uder 'if' is executed.
* Otherwise they will be igored by python & statement outside the if block will be executed
Syntax:
if <condition>:  # here 'if' is a python keyword & ':' is used in python to be more readable
 <statement to be executed> # here each line should be indented by same amount in a block of code
"""
#Ex1.0: the eligibility to vote should be >=18, we'll use a program to accept the age of the voter
age = int(input("Please enter your age "))
if age>=18:
    print("Congo, you are eligible to vote")
#Here, if you give less than 18, there will be no o/p, as it will be ignored if the if statement's
#o/p is false, so we need 'else' statement to get an over all output

# If-else
"""
syntax:
if <condition>:
  <statement to be executed> if the condition is true
else:
  <statement to be executed> if the condition is false
"""
#Ex1.1: lets finish the previous program
age = int(input("Please enter your age "))
if age>=18:
    print("Congo, you are eligible to vote")
else:
   print("sorry, you are not eligible to vote")
# If there is more than one condition we will use if-elif-else
"""
the elif statement lets us check multiple expressions for True & executes as soon as one if the 
statement is evalutes to be true
Similar to the else statement the elif part is optional, how ever here  an arbitary number of elif statement 
following an elif
Syntax:
if <condition1>:
elif <condition2>: 
elif <condition3>: 
else:
  <statement to be executed>
"""
#Ex2.0:
marks = int(input("please enter your marks "))
if marks>=90:
    print("E")
elif marks<90 and marks>=75:
    print("A")
elif marks<75 and marks>=40:
    print("B")
else:
    print("""You are super briliant!!, sell momos
       ~Tanmay Rout""")
#Nested if, is used if we want to check another condition after a condition is resolved to true
"""
in nested if construct, we can have a if-elif-else statement inside another if-elif-else construct
"""
#Ex3.0,
Username = input("Please enter your name ")
Password = int(input("Please  enter your password "))
if Username=="John":
    if Password==1234:
        print("Login Successful")
    else:
        print("incorrect password!")
else:
    print("Login Failed!")

#Ex4.0: Traffic light program
light = input("Which color is the light indicating")
if light=="Green":
    print("You may go fast")
elif light=="yellow":
    print("go slow")
else:
    print("stop")
#We ll write a script to check the highest number of win streak between three player in chess
user1 = 8
user2 = 6
user3 = 4
if (user1>user2)and(user1>user3):
    print("user1 is the winner")
elif (user2>user1)and(user2>user3):
    print("user2 is winner")
else:
    print("user3 is the winner")