# Binary Tree Cameras

Notice that its harder to decide where to place a camera if you start from the root, however starting from the bottom up we can easily indicate which node will need a camera

The trick here is to use a bottom up approach similar to [post order traversal](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/). This is because each leaf node has only one of two ways it can be monitored.

1. Placing a camera on a leaf
2. Placing a camera on the parent node of that leaf.

With the added bonus of its parent node being monitored too we can check to see which remaining monitored nodes are in a similar situation. (require a camera to be placed on itself or on its parent)

We repeat the process by treating them like 'new' nodes

0 = monitored
1 = camera
2 = monitored
