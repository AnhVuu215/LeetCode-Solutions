class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # Bước 1: Bỏ qua khoảng trắng ở đầu chuỗi
        while i < n and s[i] == ' ':
            i += 1

        # Bước 2: Kiểm tra dấu âm hoặc dương
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Bước 3: Đọc các chữ số
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        # Bước 4: Áp dụng dấu
        result *= sign

        # Bước 5: Giới hạn giá trị trong 32-bit signed integer
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result
        