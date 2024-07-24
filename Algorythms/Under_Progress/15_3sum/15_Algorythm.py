class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected result: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # Expected result: []
    print(sol.threeSum([0, 1, 1]))
    # Expected result: [[0, 0, 0]]
    print(sol.threeSum([0, 0, 0]))
