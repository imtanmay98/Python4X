# Loop statements allow us to print a statement or a group of statement multiple times

"""
'for' loop used when we know the limit of itration & while loop is used when the itration is indefinite or unknown
ex:
for i in "python":
    print(i)
    """
  #Ex1:
Number = int(input("Enter the number you want table of "))
for i in range(1,11):
    print(f"{Number}*{i}=={Number*i}")

"""
while loop  syntax,
while boolean_expression:
 statement(s)
 """
#ex2,
i = 0
while i<3:
    print("I love python")
    i += 1
# break staement: used when we need to go out of loop before it satisfies the codition
#ex3,
val = "goodmorning"
for i in val:
    if i=='m':
        break
    else:
        print(i)

#ex4,
n = 50
threshold = n*(50/100)
for i in range(0,n,10):
    if i>threshold:
        print("50% occupied")
        break
    else:
        print("passenger onboarded")




