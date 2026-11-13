# 0104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree
# Difficulty: Easy
# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
