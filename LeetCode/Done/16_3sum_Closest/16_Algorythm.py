class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        start_right = len(nums) - 1
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, start_right
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                difference = abs(target - total)

                if difference < abs(target - closest_sum):
                    closest_sum = total
                    left += 1
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
                elif difference == 0:
                    return total

        return closest_sum


if __name__ == "__main__":
    sol = Solution()
    # Expected result: 2
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))
    # Expected result: 0
    print(sol.threeSumClosest([0, 0, 0], 1))
    # Expected result: -2
    print(sol.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
