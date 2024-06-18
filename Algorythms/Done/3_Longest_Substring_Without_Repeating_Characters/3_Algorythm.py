class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ""
        for i in range(len(s)):
            result = ""
            for char in s[i:]:
                if char in result:
                    break
                result += char
            if len(result) > len(longest):
                longest = result
        return len(longest)


if __name__ == "__main__":
    sol = Solution()
    # Expected output: 3
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    # Expected output: 1
    print(sol.lengthOfLongestSubstring("bbbbb"))
    # Expected output: 3
    print(sol.lengthOfLongestSubstring("pwwkew"))
