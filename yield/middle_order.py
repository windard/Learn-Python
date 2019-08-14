'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
中序遍历得到排序数组，返回第k个值
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用递归的方法，中序遍历
        
class Solution:

    def __init__(self):
        self.counter = 0
        self.res = 0

    def kthSmallest(self, root, k):
        # 递归执行左子树的逻辑
        if root.left:
            # 不是空，才继续遍历
            self.kthSmallest(root.left, k)
        
        # 在这里执行操作，数到第 k 个即可
        self.counter += 1
        # print(root.val)
        if self.counter == k:
            # 注意：千万不能在这里返回，后序遍历还要继续进行下去
            self.res = root.val
            # 注意：这里不能加 return
            # return self.res # None
        
        # 递归执行右子树的逻辑
        if root.right:
            self.kthSmallest(root.right, k)
        return self.res


if __name__ == '__main__':
    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node2 = TreeNode(2)

    node3.left = node1
    node3.right = node4
    node1.right = node2

    solution = Solution()
    result = solution.kthSmallest(node3, k=2)
    print(result)


'''
# 使用yield迭代器进行中序递归遍历
    def gen(node):
    	if node:
    		yield from gen(node.left)
    		yield node.val
    		yield from gen(node.right)
    it = gen(node3)
    k = 3
    for _ in range(k):
    	res = next(it)
    print(res)
'''

