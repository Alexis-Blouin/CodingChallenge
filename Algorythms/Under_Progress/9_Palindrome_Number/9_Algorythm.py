class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """


if __name__ == "__main__":
    sol = Solution()
    # Expected result: True
    print(sol.isPalindrome(121))
    # Expected result: False
    print(sol.isPalindrome(-121))
    # Expected result: False
    print(sol.isPalindrome(10))
