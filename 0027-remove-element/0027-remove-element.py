class Solution(object):
    def removeElement(self, nums, val):

        k = 0   # số phần tử không bằng val

        for i in range(len(nums)):   # duyệt từng phần tử
            if nums[i] != val:       # nếu khác val thì giữ lại
                nums[k] = nums[i]   # đưa về vị trí đầu
                k = k + 1           # tăng biến đếm

        return k