# Problem

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.


# Solution

Idea:
For this problem, we simply need to prioritize the more valuable boxes first. To do this, we should sort the boxtypes array (B) in descending order by the number of units per box (B[i][1]).

Then we can iterate through B and at each step, we should add as many of the boxes as we can, until we reach the truck size (T). We should add the number of boxes added multiplied by the units per box to our answer (ans), and decrease T by the same number of boxes.

Once the truck is full (T == 0), or once the iteration is done, we should return ans.

Time Complexity: O(N log N) where N is the length of B, for the sort
Space Complexity: O(1) to O(N) depending on the sort algorithm used

[Link to Answer on Leetcode](https://leetcode.com/problems/maximum-units-on-a-truck/discuss/1271374/JS-Python-Java-C%2B%2B-or-Simple-Sort-Solution-w-Explanation)