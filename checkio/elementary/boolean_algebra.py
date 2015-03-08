# -*- encoding: utf-8 -*-
'''
Created on Mar 8, 2015

@author: lisong
In mathematics and mathematical logic, Boolean algebra is a sub-area of algebra in which 
the values of the variables are true or false, typically denoted with 1 or 0 respectively. 
Instead of elementary algebra where the values of the variables are numbers 
and the main operations are addition and multiplication, 
the main operations of Boolean algebra are the conjunction (denoted ∧), 
the disjunction (denoted ∨) and the negation (denoted ¬).

In this mission you should implement some boolean operations:
- "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
- "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
- "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. 
If x is true then the value of x → y is taken to be that of y. 
But if x is false then the value of y can be ignored; 
however the operation must return some truth value and there are only two choices,
 so the return value is the one that entails less, namely true.
- "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). 
It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
- "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.
Here you can see the truth table for these operations:
且／或／非x或y／异或／等
 x | y | x∧y  | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------
You are given two boolean values x and y as 1 or 0 and you are given an operation name as described earlier. 
You should calculate the value and return it as 1 or 0.

Input: Three arguments. X and Y as 0 or 1. An operation name as a string.

Output: The result as 1 or 0.

Example:

boolean(1, 0, "conjunction") == 0
boolean(0, 1, "exclusive") == 1

How it is used: Here you will learn how to work with boolean values and operators.
 You even get to think about numbers as booleans.

Precondition: x in (0, 1)
y in (0, 1)
operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
"conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise. 且
"disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
implication 
If x is true then the value of x → y is taken to be that of y. 
But if x is false then the value of y can be ignored; 
'''

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
def conjunction(x, y):
    res = False
    if x == 1 and y == 1:
        res = True
    return res

def disjunction(x, y):
    res = False
    if x == 1 or y == 1:
        res = True
    return res

def implication(x, y):
    x = (x + 1) % 2
    return disjunction(x, y)

def exclusive(x, y):
    res = False
    if x != y:
        res = True
    return res

def equivalence(x, y):
    res = False
    if x == y:
        res = True
    return res

OPERATION = (conjunction, disjunction, implication, exclusive, equivalence)

def boolean(x, y, operation):
    tmp = OPERATION[OPERATION_NAMES.index(operation )](x, y)
    res = 0
    if tmp:
        res = 1
        
    return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
'''
def boolean(x, y, operation):
    if operation == "conjunction": return x & y
    if operation == "disjunction": return x | y
    if operation == "implication": return (1 ^ x) | y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return x ^ y ^ 1
    return 0
'''