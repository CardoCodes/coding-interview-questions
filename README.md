## Coding Interview Practice

This table of contents will serve as a tracker of what I have completed so far.

>Excellence is an art won by training and habituation. 
>We do not act rightly because we have virtue or excellence, 
>but we rather have those because we have acted rightly. 
>We are what we repeatedly do. Excellence, then, is not an act but a habit. - Aristotle

A list of all the questions I've practiced so far may be seen here. The time complexity, languages employed, and basic idea behind the solution are all included.

| Question Name | Difficulty | Time Complexity | Topic | Language | Main Idea |
| ------------- | ---------- | --------------- | ----- | -------- | --------- |
| Two Sum | Easy | `O(n)` | Hash Tables | Python, JavaScript | Use a hash table to store and compare values of an array. This leads to faster time complexity than using a double for loop.
|  Power of Two | Easy | `O(log n)` | Binary Operations | Python, JavaScript | Binary representation and operations can be used to locate a pattern in powers of two.
| Merge Intervals | Medium| `O(n log n)` | Arrays | Python | Store the values of a 2d array in a single array and compare values, then store values needed in a new array.
| Populating Next Right Pointers Each Node | Medium | `O(n)` | Nodes | Python | Breadth first search using a queue to store values, assign node values to each other using curr.left or curr.right.
| Fib Memoization | Easy | `O(n)` | Binary Search Tree & HashMap | Python | We use a hash map to store and recall values that we already computed.
| Plus One | Easy | `O(n)` | Arrays | Python | Use a string to convert an array on ints into an integer.
| Binary Tree Cameras | Hard | `O(n)` | DFS | Python | Use dfs bottom up approach (post order traversal) to determine if the node should be a camera or monitored.
| Search Suggested Item | Medium | `O(n)` | Dict | Python | Use dictionaries to compare lists and create new array with comparison outcome |
| Short Encoding of Words | Medium | `(On)` | DFS | Python | Create a trie structure with insert then use dfs to take length of words with no children and then add them up |
| Furthest Building | Medium | `O(nlogn)` | Priority queue & Greedy | Python | use greedy method implementing a priority queue to trace where you can use bricks and ladders | 
| Kth Largest Element | Medium | `(Ologn)` | Arrays | Python | sort array and then return k element of the array |
| Course Schedule 3 | Hard | `O(nlogn)` | Heap | Python | Keep courses that work inside heap, if the current course is better fit then we swap them from heap |
| Construct Target Array With Multiple Sums | Hard | `O(n)` | Heap | Python | Use a heap to store new sums, if the num is less than the target then return false |  
| Maximum Points You Can Obtain | Medium | `O(n)`| Array | Python | Use a sliding two pointer system to calculate what distribution of left and right would be the best |
| Minimum Deletions to Make Char Freq Unique | Medium | `O(n)` | Array, Greedy | Python | count and sort frequencies of each char, then delete those that are the same frequency
| Queue Reconstruction by Height | Medium | `O(nlog)` | Array, Greedy | Python | Use the .sort function and lamda key to sort by decreasing height & within the same height group sort by increasing order of k, then insert into answer array |
| Find Pivot Index | Easy | `O(n)` | Array, Prefix Sum | Python | Use total sum of array and prefix sum to calculate the left and right side sums of the array pivot index |
| Min Moves 2 | Medium | `O(n)` | Array, Absolute Value | Python | Use the midpoint of a sorted array as the targer, then use the absolute value of i - target to find the amout of moves needed |
| Maximum Sort | Easy | `O(nlogn)` | Array, Greedy | Python | Use sorted funtion with key lambda to sort from highest boxes to lowest boxes then use gready algo to find the max boxes |
| Max Area | Medium | `O(nlogn)` | Array, Greedy | Python | Sort horizontal and vertical cuts then iterate through them and keep track of max diff |
| Interleaving String | Medium | `O(n * m)` | DP | Python | Build dp matrix to calculate solution |
| Matchsticks to Square | Medium | `O(n)` | DP, DFS | Python |  Build a dictionary for DP and find all possible ways to arrange matchsticks |
| Level Order Traversal | Easy | `O(n)` | Recursion  | Python |  Recurseive pre order traversal call dfs on right and left nodes |
| Construct Binary Tree | Medium | `O(n)` | Recursion, DFS | Python |  Recursivly create left and right subtrees by passing params |
| Invert Binary Tree | Easy | `O(n)` | Binary Tree, Recursion, DFS  | Python |  Swap left and right nodes, then use dfs to repeat the process |
| Max Area of Islands | Medium | `O(mn)` | DFS, Recursion, Matrix | Python | Use dfs on every node horizontal or veritical, set node to 0 if already visited so we do not recount. Increment count each time there is a another 1 attached to the node. |
| Out of Bounds Paths | Medium | `O(n)` | DP, Recursion | Python | Use recursion to calculate the max out of bounds moves |
| Climbing Stairs | Easy | `O(n)` | DP, Recursion | Python | Set up a helper function (DP HELPER) to calculate climbing stairs n-2 + n-1. Set up base case exits for 0,1. |
| Reverse Linked List 2 | Medium | `O(n)` | LinkedList, HashMap | Python | Set up a dummy linked list, use a hashmap to store values from l - r. Use map to resort values. |
