# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # Bắt đầu tìm kiếm từ nút gốc (root)
        current = root
        
        # Lặp cho đến khi tìm thấy nút hoặc duyệt hết cây (current trở thành None)
        while current:
            # 1. Nếu giá trị cần tìm bằng giá trị của nút hiện tại
            if val == current.val:
                # Trả về nút đó
                return current
            
            # 2. Nếu giá trị cần tìm nhỏ hơn giá trị của nút hiện tại
            elif val < current.val:
                # Di chuyển sang cây con bên trái (vì BST phải có giá trị nhỏ hơn ở bên trái)
                current = current.left
            
            # 3. Nếu giá trị cần tìm lớn hơn giá trị của nút hiện tại
            else: # val > current.val
                # Di chuyển sang cây con bên phải
                current = current.right
                
        # Nếu vòng lặp kết thúc mà không tìm thấy (current là None), trả về None
        return None
        