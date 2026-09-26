class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # nums = [3, 4, 3, 2, 5]

        # dp = [,,,,]

        def robhouse(houses):

            prev1, prev2 = 0,0

            for money in houses:
                current = max(prev1, prev2 + money)

                prev2 = prev1
                prev1 = current

            return prev1

        if n == 1:
            return nums[0]

        rob1st = robhouse(nums[:-1])
        dontrob1st = robhouse(nums[1:])

        return max(rob1st, dontrob1st)