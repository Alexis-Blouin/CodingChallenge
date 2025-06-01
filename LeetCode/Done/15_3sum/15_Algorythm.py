class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        start_right = len(nums) - 1

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, start_right
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    sol = Solution()
    # Expected result: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # Expected result: []
    print(sol.threeSum([0, 1, 1]))
    # Expected result: [[0, 0, 0]]
    print(sol.threeSum([0, 0, 0]))
