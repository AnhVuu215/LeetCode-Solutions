class Solution(object):
    def isPalindrome(self, x):
        # Số âm không bao giờ là palindrome
        if x < 0:
            return False
        
        # Số kết thúc bằng 0 (nhưng không phải 0) cũng không phải palindrome
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0

        # Đảo một nửa số
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Nếu độ dài lẻ → bỏ đi số giữa
        return x == reversed_half or x == reversed_half // 10
