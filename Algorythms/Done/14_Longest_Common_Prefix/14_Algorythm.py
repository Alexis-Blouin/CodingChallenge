class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type height: List[int]
        :rtype: int
        """
        prefix = ""
        smallest_word = min(strs, key=len)
        for i in range(len(smallest_word)):
            new_letter = strs[0][0]
            for ii in range(1, len(strs[1:]) + 1):
                if strs[ii][0] != new_letter:
                    return prefix
                strs[ii] = strs[ii][1:]

            strs[0] = strs[0][1:]
            prefix += new_letter

        return prefix


if __name__ == "__main__":
    sol = Solution()
    # Expected result: "fl"
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    # Expected result: ""
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
