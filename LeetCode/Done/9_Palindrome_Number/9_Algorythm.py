class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        return str_x == str_x[::-1]


if __name__ == "__main__":
    sol = Solution()
    # Expected result: True
    print(sol.isPalindrome(121))
    # Expected result: False
    print(sol.isPalindrome(-121))
    # Expected result: False
    print(sol.isPalindrome(10))
