class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


if __name__ == "__main__":
    sol = Solution()
    # Expected result: 49
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # Expected result: 1
    print(sol.maxArea([1, 1]))
