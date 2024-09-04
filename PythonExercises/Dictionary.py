# It contaion the values in key & value format, where key is immutable , values are mutable
# key & values are separated by ':' & the whole thing is enclosed by '{}' .
#ex1,
courses_students_enrolled = {"danny":["Python","selenium"], "kimmy":["Java","selenium"], "popol":"ruby"}
print(courses_students_enrolled)

#these are the operations we perform in the dictionary
"""
1. accessing elements of a dictionary
2. updating the dictionary
3. deleting elements from the dictionary
Note: since dictionary's elements are unorder so we can't perform indexing & access them
"""
#for fetching the elements of the dictionary we need the key,
# so we can use it in [] or with get() method, the difference is, for sqare braces we get
# keyerror incase key is not found where with () it returns none if the key is not found

#replacing the values of a dictionary
examp = {1:"java",2:"javascript"}
examp[1] = "python"
examp[2] = "selenium"
print(examp.get(1))
print(examp)
del examp[1]
print(examp) # throughs NameExrror

# in the above, we replaced the key values, if we didn't have those key  it would have added new key value pair
dict2 = {11:"mohan",12:"rama",13:"gopal"}
print(dict2.keys())
print(dict2.items()) # returns o/p in tuple form
print(dict2.clear())