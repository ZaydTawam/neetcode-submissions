class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        start_of_cycle = nums[0]
        while slow != start_of_cycle:
            slow = nums[slow]
            start_of_cycle = nums[start_of_cycle]
        
        return start_of_cycle

