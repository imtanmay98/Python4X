#modules are the pre-wriiten code which will help us build our code
"""
syntax:
import module_name

but if we need to import some specific code, we don't need to import the whole module,
we can just use "from" key  word
syntax:
from module_name import something # here something is a part from the module which can be a function,
class or a static variable.
"""

"""
lets us assume we want to use all the math functions which includes trigonometri, representation
function, angle conversion functions etc.
ex: import math
Ex2: below are the commonly used math function,
1. ceil(x) - returns the smallest integer grater than or equal to x
2. floor(x) - returns the largest integer less than or equal to X
3. fab(x) - returns the bestabsolute value
4. factorial(x) - returns the factorial  of x
5. fmod(x,y) - returns the rerminder when 
6.log2(x)- returns the base 2 logarithm
pow(x,y) - returning x raied


"""

import math
radius = int(input("enter the radius of the circle "))
Area_of_circle = math.pi*radius*radius
print("Area of circle is",Area_of_circle )