class Solution(object):
    def mySqrt(self, x):
        left, right = 0, x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid        # mid có thể là kết quả
                left = mid + 1   # thử lớn hơn
            else:
                right = mid - 1  # giảm xuống

        return ans
