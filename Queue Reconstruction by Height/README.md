# Problem

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

# Solution

Its important to note that the only key part of the problem that matters is the amount of people that are taller & infront of them.

If we add people in order from tall to short then the next persons position in the array is just their k value.

Sort people by height from tallest to shortest first, and then by their K values. Then we use greedy so that we can insert into the answer array using person[1] as the index we must insert the person into the queue.