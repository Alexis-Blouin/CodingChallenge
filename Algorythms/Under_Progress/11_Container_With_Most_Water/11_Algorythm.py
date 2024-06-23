class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        unsorted_height = [x for x in height]
        height.sort()
        max_pos_1 = unsorted_height.index(height[len(height) - 1])
        i = 2
        while i <= len(height) - 1 and unsorted_height.index(
            height[len(height) - i]
        ) == unsorted_height.index(height[len(height) - 1]):
            print(
                unsorted_height.index(height[len(height) - i]),
                unsorted_height.index(height[len(height) - 1]),
            )
            i += 1
        if i > len(height) - 1:
            return height[max_pos_1]
        max_pos_2 = unsorted_height.index(height[len(height) - i])
        print(max_pos_1, max_pos_2)
        return unsorted_height[max_pos_2] * abs(max_pos_1 - max_pos_2)


if __name__ == "__main__":
    sol = Solution()
    # Expected result: 49
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # Expected result: 1
    print(sol.maxArea([1, 1]))
    # TODO Add loop that checks every bigest column possibilities and then look for the biggest span between them and the second biggest column
    # Expected result: 16
    print(sol.maxArea([4, 3, 2, 1, 4]))
