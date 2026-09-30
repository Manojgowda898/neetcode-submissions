class Solution:
    def countSubstrings(self, s: str) -> int:

        totalP = 0

        n = len(s)

        dp = [ [False] * n for _ in range(n)]

        for startIdx in range(n - 1, -1, -1):

            for endIdx in range(startIdx, n):

                if s[startIdx] == s[endIdx] and (endIdx - startIdx  <= 2 or dp[startIdx + 1][endIdx - 1] ):
                    dp[startIdx][endIdx] = True
                    totalP += 1

        return totalP


        