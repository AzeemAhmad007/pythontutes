# Docstrings in python
# Python docstrings are the string literals that appear
# right after the definition of a function, method, class, or module.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)# used to  get docstring

# docstring is not ignored as  comments completely ignored its just used to define the function
a=40
b=30

def isgreater(a,b):
    """this function is used to check which number is greater"""
    if a > b:
        print("First number is greater, 2nd way")
    else:
        print("second number is greater , 2nd way")
isgreater(a,b)
print(isgreater.__doc__)




"""PEP 8
PEP 8 is a document that provides guidelines and best practices on how to write Python code.
It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. 
The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them.
 A PEP is a document that describes new features proposed for Python
 and documents aspects of Python, like design and style, for the community."""

#Easter egg
import this  # in  terminal

"""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the r
ules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to
 guess.
There should be one-- and preferably only one --ob
vious way to do it.
Although that way may not be obvious at first unle
ss you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a b
ad idea.
If the implementation is easy to explain, it may b
e a good idea.
Namespaces are one honking great idea -- let's do
more of those!
>>>
"""
