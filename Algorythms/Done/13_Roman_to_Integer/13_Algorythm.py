class Solution(object):
    def romanToInt(self, s):
        """
        :type height: List[int]
        :rtype: int
        """
        sum = 0
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        last_char = s[0]
        for char in s[1:]:
            if symbols[last_char] < symbols[char]:
                sum -= symbols[last_char]
            else:
                sum += symbols[last_char]
            last_char = char
        return sum + symbols[last_char]


if __name__ == "__main__":
    sol = Solution()
    # Expected result: 3
    print(sol.romanToInt("III"))
    # Expected result: 58
    print(sol.romanToInt("LVIII"))
    # Expected result: 1994
    print(sol.romanToInt("MCMXCIV"))
