# placing a hash tag in front of a line will make the 
#line not execute 
# this is referred to as a "comment"


'''
line 1 of comment 
line 2 of comment 
line 3 of comment
'''

"""
line 1 of comment 
line 2 of comment 
line 3 of comment
"""

"""
A condition is a comparison.
Conditions evaluate a boolean value to be true or false.
is a condition is true, the following block of code will run. 
a block of code will be indented.

COMPARISONS:
>      Greater than
<      less than 
<=     less than or equal to 
>=    greater than or equal to 
==     equal to
!=      not  equal to 
"""


mark = int(input("please enter your mark:"))

if mark >= 90:
    print("you aced it!")
    
elif mark >= 70:
    print ("you got a B! good job")
    
elif mark >= 60:
    print("thats a C!")


elif mark >= 50:
    print("you barely made it!")
    
    
else:
    print("you faild!")
    
    
if (mark > 0 and mark <= 100):
    print("you have a valid mark")
    

if (mark > 100 or mark <= 0):
    print("this is an invalid mark")
    
    
    
    
    ''strings are a datatype 
    strings can be changed 
    strings are writen within single or double quotashion marks 
    all usrs input are strings.
