class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        cycle_start = nums[0]
        while slow != cycle_start:
            slow = nums[slow]
            cycle_start = nums[cycle_start]
        
        return cycle_start


