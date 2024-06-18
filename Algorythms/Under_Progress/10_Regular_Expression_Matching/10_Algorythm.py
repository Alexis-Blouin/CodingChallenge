class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


if __name__ == "__main__":
    sol = Solution()
    # Expected result: False
    print(sol.isMatch("aa", "a"))
    # Expected result: True
    print(sol.isMatch("aa", "a*"))
    # Expected result: True
    print(sol.isMatch("ab", ".*"))
