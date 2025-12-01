# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def find_min_value_node(self, node):
        """
        Hàm helper tìm nút có giá trị nhỏ nhất trong cây con (phần tử kế nhiệm).
        Nút nhỏ nhất luôn nằm ở cùng cực bên trái.
        """
        current = node
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # Trường hợp cơ sở: Cây rỗng
        if not root:
            return root

        # 1. Tìm kiếm nút cần xóa (Dùng đệ quy)
        if key < root.val:
            # Nếu key nhỏ hơn, tìm kiếm tiếp ở cây con bên trái
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Nếu key lớn hơn, tìm kiếm tiếp ở cây con bên phải
            root.right = self.deleteNode(root.right, key)
        
        # 2. Đã tìm thấy nút cần xóa: (key == root.val)
        else:
            # Trường hợp A: Nút không có con hoặc chỉ có một con
            
            # Nếu không có con trái (hoặc là nút lá)
            if not root.left:
                temp = root.right
                # Xóa nút gốc hiện tại (root)
                # Đổi chỗ nút gốc hiện tại (nút đã bị xóa) bằng con phải của nó
                return temp
            
            # Nếu không có con phải
            elif not root.right:
                temp = root.left
                # Xóa nút gốc hiện tại (root)
                # Đổi chỗ nút gốc hiện tại (nút đã bị xóa) bằng con trái của nó
                return temp
            
            # Trường hợp B: Nút có đủ hai con
            
            # 2a. Tìm nút kế nhiệm (Inorder Successor) - nút có giá trị nhỏ nhất ở cây con bên phải
            successor_node = self.find_min_value_node(root.right)
            
            # 2b. Sao chép giá trị của nút kế nhiệm vào nút hiện tại (nút cần xóa)
            root.val = successor_node.val
            
            # 2c. Xóa nút kế nhiệm (successor_node) khỏi cây con bên phải
            # Nút kế nhiệm chắc chắn chỉ có tối đa một con (con phải), 
            # nên việc xóa nó sẽ rơi vào Trường hợp A (đã xử lý ở trên)
            root.right = self.deleteNode(root.right, successor_node.val)

        # Trả về gốc của cây con đã được thay đổi/xử lý
        return root