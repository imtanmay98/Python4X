#Following are the types of operators,
"""
1. Arithmatic
2. Relational
3. logical
4. Membership and Identity
5. Bitwise
6. Walrus
"""
#Lets discuss them one by one
"""
Arithmatic
###########
It genarally takes two operands &perform a calculation among them
these are the following arithmatic operators
1. +Addition: adds two operands
2. -subtraction: subtracts 
3. *Multiplication
4. /Division
5. %Modulus
6. **Exponent
7. //Trucation or floor division
"""
#Ex,
a = 5
b = 4
c = a+b
print("Addition is",c)
print(5+4)

#EX2,
num1 = 5
num2 = 2
print("Module is",num1%num2) # o/p = 1
print("Floor division is", num1//num2)#o/p = 2

#EX3,
NumberOne = 5
NumberTwo = 2
NumberThree =  NumberOne**NumberTwo
print("Exponet is",NumberThree)

#Comparision operator
"""
Used for comparing, returns valu True/False according to the condition
Types,
1. >Greater than, returns true if left side operand is greater than the right one
2. <Less than , returns true if left side operand is smaller than the right one
3. == Equals to , returns true if both side operands are equal
4. != Not equal , returns true if both side operands are not equal
5. >=Greater than or equals to, returns true if left side operand is greater than or equal to the right one
6. <=Less than or equals to, returns true if left side operand is smaller than or equal to the right one

"""
#Ex4,

age = 16
requiredAge = 18
print(age>requiredAge)

#Ex5,
age1 = 18
requiredAge1=18
print(age1==requiredAge1)

"""
Logical Operator,
1. and, returns true if both operands are true
2. or, returns true if either of the operands is true
3. not, returns true if the operand is false
"""
#EX6,
X = True
Y = False
print(X and Y)
print(X or Y)
print(not X)

#Ex7,

NUM1 = 5
NUM2 = 8
print(NUM1>NUM2 or NUM1<NUM2)

"""
Membership operantor,
1. in, returns true if the value is found in the sequence
2. not in, returns true if the value is not found in the  sequence
"""
#EX8,
name1 = "pythonx"
print('x' in name1)
print('x' not in name1)

"""
Identity operator, used to check if the two value of the variable are stored in one place

"""
#Ex9,
num4 = 4
print(id(num4))
"""
types,
1. is, returns true if the operands are identical
2. not is, returns true if the operands are not identical
"""
#Ex10,
N1 = 8
N2 = 8
N3 = 0
print(N1 is N2)
print(N1 is not N2)
print(N1 is N3)
print(id(N1))
print(id(N2))

"""
Walrusoperator, new assignment operator used to assign variables within an expression
:=, it combines the steps of declarion and implementation in at the same time
"""
#Ex11,

print(MyName:= "Ram")
