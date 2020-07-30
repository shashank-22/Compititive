class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = ""
        
        def preorder(node,treestr):
            if(not node):
                treestr+=",p"
                return treestr
            treestr+="," + str(node.val)
            
            if(not node.left and not node.right):
                treestr+=",L"
                return treestr
            else:
                if(node.left):
                    treestr=preorder(node.left,treestr)
                else:
                     treestr+=",p"
                if(node.right):
                    treestr=preorder(node.right,treestr)
                else:
                     treestr+=",p"
                return treestr
        
        kk= preorder(root,tree)[1:]
        print(kk)
        return kk

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(data=="p"):
            return None
        data = data.split(",")
        # print(data)
        index=0
        stack = []
        root = TreeNode(int(data[index]))
        currnode = root
        index+=1
        while(index<len(data)):
            if(data[index]=='L' and len(stack)==0):
                break
            elif(data[index]=='L' and len(stack)!=0):
                currnode = stack[-1]
                stack.pop(-1)
            elif(data[index]!='p'):
                temp = TreeNode(int(data[index]))
                if(not currnode.left):
                    stack.append(currnode)
                    currnode.left = temp
                    currnode = temp
                else:
                    currnode.right = temp
                    currnode = temp
            elif(data[index]=='p'):
                if(currnode.left):
                    if(len(stack)==0):
                        break
                    currnode = stack[-1]
                    stack.pop(-1)
                else:  
                    index+=1
                    temp = TreeNode(int(data[index]))
                    currnode.right = temp
                    currnode = temp
            index+=1
        return root