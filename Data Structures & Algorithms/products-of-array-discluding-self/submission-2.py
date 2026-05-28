class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]
        post = [1]
        for i in range(1, n):
            pre.append(pre[i-1]*nums[i-1])
            post.append(post[i-1]*nums[n-i])
        post = post[::-1]
        res = []
        for i in range(n):
            res.append(pre[i]*post[i])
        
        return res




        
        # products = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     products.append(product)
        # return products