class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pal = s[0]
        for center in range(len(s)):
            # Check for odd-length palindrome centered at center
            left, right = center, center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            pal = s[left : right + 1] if right - left + 1 > len(pal) else pal

            # Check for even-length palindrome centered at center and center+1 (if possible)
            if center < len(s) - 1 and s[center] == s[center + 1]:
                left, right = center, center + 1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                left += 1
                right -= 1
                pal = s[left : right + 1] if right - left + 1 > len(pal) else pal

        return pal


if __name__ == "__main__":
    sol = Solution()
    # Expected output: "bab"
    print(sol.longestPalindrome("babad"))
    # Expected output: "bb"
    print(sol.longestPalindrome("cbbd"))
