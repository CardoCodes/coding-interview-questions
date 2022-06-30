# Problem

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

# Solution

Its important to notice that if you sort the array and then subtract or add 1 from left and right side the numbers will always become equal near the middle.

In order to implement this we can create sort the array and calculate the midpoint value. After that we can use the absolute value of each i - mid to calulate the amount of moves required to make the whole array equal.