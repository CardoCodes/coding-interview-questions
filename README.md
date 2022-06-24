## Coding Interview Practice

This table of contents will serve as a tracker of what I have completed so far.

>Excellence is an art won by training and habituation. 
>We do not act rightly because we have virtue or excellence, 
>but we rather have those because we have acted rightly. 
>We are what we repeatedly do. Excellence, then, is not an act but a habit. - Aristotle

A list of all the questions I've practiced so far may be seen here. The time complexity, languages employed, and basic idea behind the solution are all included.

| Question Name | Difficulty | Time Complexity | Topic | Language | Main Idea |
| ------------- | ---------- | --------------- | ----- | -------- | --------- |
| Two Sum | Easy | `O(n)` | HashTables | Python, JavaScript | Use a hash table to store and compare values of an array. This leads to faster time complexity than using a double for loop.
|  Power of Two | Easy | `O(log n)` or `O(n)` | Binary Operations | Python, JavaScript | Binary representation and operations can be used to locate a pattern in powers of two.
| Merge Intervals | Medium| `O(n log n)` | Arrays | Python | Store the values of a 2d array in a single array and compare values, then store values needed in a new array.
| Populating Next Right Pointers Each Node | Medium | `O(n)` | Nodes | Python | Breadth first search using a queue to store values, assign node values to eachother using curr.left or curr.right.
| Fib Memoization | Easy | `O(n)` | Binary Search Tree & HashMaps | Python | We use a hashmap to store and recall values that we already computed.
| Plus One | Easy | `O(n)` | Arrays | Python | Use a string to convert an array on ints into an integer.
| Binary Tree Cameras | Hard | `O(n)` | DFS | Python | Use dfs bottom up approach (postorder traversal) to determine if the node should be a camera or monitored.
| Search Suggested Item | Medium | `O(n)` | Dict | Python | Use dictionaries to compare lists and create new array with comparison outcome |
| Short Encoding of Words | Medium | `(On)` | DFS | Python | Create a trie structure with insert then use dfs to take length of words with no children and then add them up |
| Furthest Building | Medium | `O(nlogn)` | Priority queue & Greedy | Python | use greedy method implementing a priority queue to trace where you can use bricks and ladders | 
| Kth Largest Element | Medium | `(Ologn)` | Arrays | Python | sort aray and then return k element of the array |
| Course Schedule 3 | Hard | `O(nlogn)` | Heap | Python | Keep courses that work inside heap, if the current course is better fit then we swap them from heap |
| Construct Target Array With Multiple Sums | Hard | `O(n)` | Heap | Python | Use a heap to store new sums, if the num is less than the target then return false |  