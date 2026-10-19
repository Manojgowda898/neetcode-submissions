class Solution:
    def numDecodings(self, s: str) -> int:
        # This is the recursion method with memoization to store each ways and return if its in the dict before checking the ways of the currindex
        memo = {}

        def dfs(i):

            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            ways = dfs( i + 1)

            if i + 1 < len(s):

                currnum = int(s[i: i+ 2])

                if 10 <= currnum <= 26:
                    ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)

   