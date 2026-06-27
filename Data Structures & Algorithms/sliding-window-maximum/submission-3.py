from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r - l + 1 > k:
                if q[0] == l:
                    q.popleft()
                l += 1

            if r - l + 1 == k:
                res.append(nums[q[0]])
        
        return res