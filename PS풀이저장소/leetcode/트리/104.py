# 104.Maximum Depth of Binary Tree
class Solution:        
    def maxDepth(self, root: Optional[TreeNode]):    
        result = 0
        if not root:
            return 0
        
        def dfs(x, count):
            #print(x.val, count)
            nonlocal result
            
            if x.left != None:
                dfs(x.left, count+1)
                
            if x.right != None:
                dfs(x.right, count+1)
                
            if x.left == None and x.right == None:
                result = max(result, count)
            return
        
        dfs(root, 1)
        
        return result