from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        stk = deque()

        l = 0
        for r in range(len(nums)):
            while stk and nums[r] > nums[stk[-1]]:
                stk.pop()
            stk.append(r)

            if r - l + 1 == k:
                res.append(nums[stk[0]])
                if stk[0] == l:
                    stk.popleft()
                l += 1
        return res


# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation:
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2   [2,1]
#  1 [2  1  0] 4  2  6        2   [2,1,0]
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6
