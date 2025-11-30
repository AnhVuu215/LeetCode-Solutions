class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) < 2:
            return s

        start, max_len = 0, 1

        # Hàm mở rộng từ center
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # trả về substring palindrome
            return left + 1, right - 1

        for i in range(len(s)):
            # TH1: palindrome độ dài lẻ (1 center)
            l1, r1 = expand(i, i)
            if r1 - l1 + 1 > max_len:
                start = l1
                max_len = r1 - l1 + 1

            # TH2: palindrome độ dài chẵn (2 center)
            l2, r2 = expand(i, i + 1)
            if r2 - l2 + 1 > max_len:
                start = l2
                max_len = r2 - l2 + 1

        return s[start:start + max_len]
