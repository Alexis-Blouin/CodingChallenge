class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        start_right = len(nums) - 1

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

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
    # Expected result: 2
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))
    # Expected result: 0
    print(sol.threeSumClosest([0, 0, 0], 1))
