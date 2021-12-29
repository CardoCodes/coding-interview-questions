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
| Populating Next Right Pointers Each Node | Medium | O(n) | Nodes | Python | Breadth first search using a queue to store values, assign node values to eachother using curr.left or curr.right.