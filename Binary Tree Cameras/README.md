# Binary Tree Cameras

Notice that its harder to decide where to place a camera if you start from the root, however starting from the bottom up we can easily indicate which node will need a camera

The trick here is to use a bottom up approach similar to [postorder traversal](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/). This is because each leaf node has only one of two ways it can be monitored

1. Placing a camera on a leaf
2. Placeing a camera on the parent node of that leaf

