class Solution(object):
    def searchRange(self, nums, target):
        def binarySearch(nums, target, findFirst):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    result = mid
                    if findFirst:
                        right = mid - 1  # Tìm vị trí đầu
                    else:
                        left = mid + 1   # Tìm vị trí cuối
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        first = binarySearch(nums, target, True)
        last = binarySearch(nums, target, False)
        
        return [first, last]