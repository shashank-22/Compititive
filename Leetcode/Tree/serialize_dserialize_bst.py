# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(root):
            if not root:
                return
            preorder.tree +=" "+str(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder.tree = ""
        preorder(root)
        return preorder.tree
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if(data==""):
            return None
        def buildTree(start,end):
            
            if(start>end):
                return None
            curnode = TreeNode(buildTree.preorder[buildTree.index])
            buildTree.index+=1
            if(start == end):
                return curnode
            inorderindex = buildTree.map[curnode.val]
            
            curnode.left = buildTree(start,inorderindex-1)
            curnode.right = buildTree(inorderindex+1,end)
            return curnode
        
        buildTree.preorder = list(map(int,data.strip().split(" ")))
        buildTree.inorder = sorted(buildTree.preorder)
        buildTree.index = 0
        buildTree.map = {}
        for i,val in enumerate(buildTree.inorder):
            buildTree.map[val] = i
        
        return buildTree(0,len(buildTree.preorder)-1)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))