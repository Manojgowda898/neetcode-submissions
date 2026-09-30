class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        reslen = 0

        def palindromechecker(l, r):
            bestIdx = -1
            bestLen = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:

                currlen = r - l + 1

                if currlen > bestLen:
                    bestIdx = l
                    bestLen = currlen

                l -= 1
                r += 1

            return bestIdx, bestLen

        for i in range(len(s)):

            for l, r in [(i, i), (i, i + 1)]:

                idx, length = palindromechecker(l, r)

                if length > reslen:
                    resIdx = idx
                    reslen = length

        return s[resIdx:resIdx + reslen]