class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """


if __name__ == "__main__":
    # Expected output: 42
    print(Solution().myAtoi("42"))
    # Expected output: -42
    print(Solution().myAtoi("   -42"))
    # Expected output: 1337
    print(Solution().myAtoi("1337c0d3"))
    # Expected output: 0
    print(Solution().myAtoi("0-1"))
    # Expected output: 0
    print(Solution().myAtoi("words and 987"))
