# -*- coding:utf-8 -*-
"""
tests of python function doc string
"""

def my_function():
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    pass

if __name__ == '__main__':
    print my_function.__doc__
    print '------------------------'
    print help(my_function)