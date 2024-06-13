class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]

        array = [[], []]
        i = 0
        ii = 0
        space = numRows - 2
        for char in s:
            if array == []:  # Initialize the array if empty
                array = [[None] * len(s) for _ in range(numRows)]
            print(i, ii, char)
            array[i][ii] = char
            ii += 1
            if ii == numRows:
                for j in reversed(range(space)):
                    i += 1
                    array[i][j] = char


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))
    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))
    s = "A"
    numRows = 1
    print(Solution().convert(s, numRows))
