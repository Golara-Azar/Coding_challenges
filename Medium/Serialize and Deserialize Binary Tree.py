# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str

        O(n) time for recursion on all nodes
        O(n) to keep the tree nodes in string
        """
        res = ""
        if root is None:
            return "#"
        res+=str(root.val)
        res+=','
        res+=self.serialize(root.left)
        res+=','
        res+=self.serialize(root.right)
        
        return res
        

    def deserialize(self, data_str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode

        O(n) time to traverse the list
        O(n) space to keep each node value in the list and the stack
        """
        
        if len(data_str)<=1:
            return None
        data = data_str.split(",")
        
        dummy = tree = TreeNode(eval(data[0]))
        prev = [tree]
        i = 1
        while i<len(data):
            
            while data[i]!='#':
                prev.append(tree)
                
                
            
                
                tree.left = TreeNode(eval(data[i]))
                tree = tree.left
                
                i+=1
                if i==len(data):
                    
                    return dummy
                
            prev.append(tree)   
            while data[i]=='#':
                if len(prev)>0:
                    tree = prev.pop()
                    
                i+=1
                if i==len(data):
                    
                    return dummy
             
            
            tree.right = TreeNode(eval(data[i]))
            
            tree = tree.right
            
            i+=1
            if i==len(data):
                    
                    return dummy
            
            
        
        return dummy
            
            
            
            
            
            
                
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
