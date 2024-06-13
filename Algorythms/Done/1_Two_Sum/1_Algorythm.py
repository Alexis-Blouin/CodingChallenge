from collections import deque

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""


class Solution(object):
    def twoSum(nums, target):
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
    print(Solution.twoSum([2, 7, 11, 15], 9))
