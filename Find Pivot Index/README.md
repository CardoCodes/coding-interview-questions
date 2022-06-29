# Problem

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

# Solution

Its important to note that if we calculate the sum every time, we will run into runtime errors with large lists. The best approach is to calculate the sum then use prefix or postfix sum to calculate the left or right side.

In this case we calculate the sum first and then traverse the array to calculate the right and left side. Once the left and right sides match we return the index
