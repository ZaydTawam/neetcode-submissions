class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i, num in enumerate(nums):
            diff = target-num
            if diff in elements:
                return [elements[target-num], i]
            elements[num] = i