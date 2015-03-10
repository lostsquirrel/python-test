# -*- coding:utf-8 -*-
'''
Created on 2015-03-10

@author: lisong
In computer science and discrete mathematics, 
an inversion is a pair of places in a sequence 
where the elements in these places are out of their natural order. 
So, if we use ascending order for a group of numbers, 
then an inversion is when larger numbers appear before lower number in a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions
- 5 and 3; - 5 and 4; - 7 and 6.

You are given a sequence of unique numbers 
and you should count the number of inversions in this sequence.

Input: A sequence as a tuple of integers.

Output: The inversion number as an integer.

Example:

count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
count_inversion((0, 1, 2, 3)) == 0
    
1
2
3
How it is used: In this mission you will get to experience the wonder of nested loops, that is of course, if you don't use advanced algorithms.

Precondition: 2 < len(sequence) < 200
len(sequence) == len(set(sequence))
all(-100 < x < 100 for x in sequence)

 If i < j and A(i) > A(j), then the pair (i, j) is called an inversion of A.[1][2]
'''
def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    amount = len(sequence)
    count = 0
    for x in range(0, amount):
        for y in range(x + 1, amount):
            if (x < y and sequence[x] > sequence[y]):
#                 print x, y''
                count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    
    '''
    def count_inversion(sequence):
    return sum(sum(m<n for m in sequence[i+1:]) for i,n in enumerate(sequence))
    '''