class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums)-1
        avg = []

        while left < right:
            value = (nums[left]+nums[right]) / 2
            avg.append(value)
            left += 1
            right -= 1
        
        return min(avg)
            

        
        