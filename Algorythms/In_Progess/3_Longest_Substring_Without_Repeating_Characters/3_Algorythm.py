class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        i = 0
        for char in s:
            if char in result:
                break
            result.append(char)
            i += 1
        return i


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
