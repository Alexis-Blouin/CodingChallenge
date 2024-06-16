class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        i = 0
        ii = 0

        while ii < len(nums2):
            while i < len(nums1):
                if nums1[i] < nums2[ii]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    break
            if ii < len(nums2):
                nums3.append(nums2[ii])
                ii += 1
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1

        l = len(nums3)
        if (l % 2) == 0:
            return float(nums3[l // 2] + nums3[~(l // 2)]) / 2
        else:
            print(l)
            return nums3[l // 2]


if __name__ == "__main__":
    # Expected output: 2.0
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    # Expected output: 2.5
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
