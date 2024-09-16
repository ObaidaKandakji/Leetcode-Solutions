class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        nums_set = set(nums)

        for num in nums:
            if num + diff in nums_set and num + 2 *diff in nums_set:
                count += 1

        return count