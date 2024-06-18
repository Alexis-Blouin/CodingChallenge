class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """


if __name__ == "__main__":
    sol = Solution()
    # Expected result: "MMMDCCXLIX"
    print(sol.intToRoman(3749))
    # Expected result: "LVIII"
    print(sol.intToRoman(58))
    # Expected result: "MCMXCIV"
    print(sol.intToRoman(1994))
