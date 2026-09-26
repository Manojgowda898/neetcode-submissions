class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        dp = [0] * n

        #nums = [3,5,6,2,1,6,8,4,7]

        # dp  = [3,5,9,7,10,13,18,17,25]

        dp[0], dp[1] = nums[0], max(nums[0],nums[1])

        for i in range(2,n):

            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i])

        return dp[-1]
