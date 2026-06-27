from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        l, r = 0, -1

        while r < len(nums) - 1:
            r += 1

            while q and q[-1] < nums[r]:
                q.pop()
            
            q.append(nums[r])

            if r - l + 1 > k:
                if q[0] == nums[l]:
                    q.popleft()
                l += 1

            if r - l + 1 == k:
                res.append(q[0])
        
        return res
            


# [1,2,1,0,4,2,6]
#          -----
# [6]
# [2,2,4,4,6]