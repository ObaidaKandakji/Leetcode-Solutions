class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)  # Create a result list of the same size
        left, right = 0, len(nums) - 1
        position = right  # Start filling from the largest index

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[position] = nums[left] ** 2
                left += 1
            else:
                ans[position] = nums[right] ** 2
                right -= 1
            position -= 1

        return ans
