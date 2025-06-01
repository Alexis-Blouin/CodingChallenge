from collections import deque


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        ii = 1
        queue = deque(nums)  # at least one element in the queue to kick start bfs
        while len(queue) > 0:  # as long as there is an element in the queue
            node = queue.popleft()  # dequeue
            for num in queue:  # enqueue children
                if node + num == target:  # early return if problem condition met
                    return [i, ii]

                ii += 1
            i += 1
            ii = i + 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    # Expected output: [0, 1]
    print(sol.twoSum([2, 7, 11, 15], 9))
    # Expected output: [1, 2]
    print(sol.twoSum([3, 2, 4], 6))
    # Expected output: [0, 1]
    print(sol.twoSum([3, 3], 6))
