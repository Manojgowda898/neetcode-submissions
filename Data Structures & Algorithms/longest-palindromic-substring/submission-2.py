class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Length of the string
        strlen = len(s)

        # dp[startIdx][endIdx] tells us whether
        # s[startIdx : endIdx + 1] is a palindrome
        dp = [[False] * strlen for _ in range(strlen)]

        # Starting index of the longest palindrome found
        resIdx = 0

        # Length of the longest palindrome found
        reslen = 0

        # Start from the end of the string and move backwards
        for startIdx in range(strlen - 1, -1, -1):

            # Check every possible ending index
            for endIdx in range(startIdx, strlen):

                # First and last characters must be equal
                first_and_last_match = (
                    s[startIdx] == s[endIdx]
                )

                # The inside must also be a palindrome.
                #
                # endIdx - startIdx <= 2 means the substring
                # has at most 3 characters, so checking the
                # first and last characters is enough.
                is_inside_palindrome = (
                    endIdx - startIdx <= 2
                    or dp[startIdx + 1][endIdx - 1]
                )

                # Both conditions must be true
                if first_and_last_match and is_inside_palindrome:

                    # Mark this substring as a palindrome
                    dp[startIdx][endIdx] = True

                    # Length of current palindrome
                    currlen = endIdx - startIdx + 1

                    # If current palindrome is longer than
                    # the previous longest palindrome
                    if reslen < currlen:

                        # Save its starting index
                        resIdx = startIdx

                        # Save its length
                        reslen = currlen

        # Return the longest palindrome
        return s[resIdx : resIdx + reslen]