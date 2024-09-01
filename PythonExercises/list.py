#list allow us to store multiple values in a single variables
"""
1. these are mutable that means the vaues in the list can be changable
2. it also allows us to store duplicate values
3. list stores ordered values.
4. values in the list are comma separated & placed in []
5. List can store values of different data types

ex1:,
List = []1,4,6,3]

"""
#ex2,
courses = ["python","java","selenium","sql","html"]
print(courses)
print(courses[:4:2])

"""
we can manupulate the list  with,
1. list slicing
2. list updating
3. deleting elements from a list
"""

#ex3,
marks = [45,55,65,35]
marks[3] = 44 # updated the value of 3rd posttion with 44
print(marks)
del marks[1]
print(marks) # delted  using del funtion

"""
operations on list
*****************
1. concatination(+)
2. repreatation(*)
3. membership 
"""
#1.
lst1 = [1,2,3]
lst2 = [4,5,6]
print(lst1+lst2) #[1, 2, 3, 4, 5, 6]
print([lst1]*2)

#membership, we have already read in the operators regarding 'in' membership operaato how it gives
#'true' o/p  we will use here,
print(8 in lst1)
print(2 in lst1)

# list  comprehemnsion
even_number = [x for x in range(1,11) if x%2==0]
print(even_number)
"""
x is the output expression
input sequence is range
x is the variable
if x%2==0 conditional part
"""

















