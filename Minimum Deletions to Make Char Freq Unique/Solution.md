# Problem

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Solution

It is important to note that the actual letters do not matter in this problem only the frequency.

We want to find the min number of deletions. To do this we can count and sort the frequency of each character. In this case we sort it in reverse order so that we can find the next unused frequency with ease.

There can only be a max frequencies of len(s). Which means we can use this to count up the max number of deletions needed to reach the correct frequency.