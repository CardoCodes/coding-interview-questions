# Problem

You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

# Solution

The trick to this problem is realizing that if the horizontal slices and vertical slices are perpendicular, then all vertical slices cross all horizontal slices. This means that we just need to find the largest of each, and the cross-section should be the largest slice.

To find the largest slice of each, we need to first sort the horizontal cuts (hc) and vertical cuts (vc), then iterate through both sets and keep track of the maximum difference found between two consecutive cuts (maxh, maxv). We need to not forget to include the two end cuts, which are found using 0 and h/w, as well.

Once we have the largest difference for both, we can just return the product of these two numbers, modulo 1e9+7.

[Link](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/1248591/JS-Python-Java-C%2B%2B-or-Simple-Sort-and-Iterate-Solution-w-Explanation)