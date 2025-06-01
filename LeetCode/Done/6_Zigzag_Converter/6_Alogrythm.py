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

        numIterations = 2 * numRows - 2
        i = 0
        result = ""
        while i < numRows:
            if i == 0 or i == numRows - 1:
                j = 0
                while j + i < len(s):
                    result += s[j + i]
                    j += numIterations
            else:
                j = 0
                while j + i < len(s):
                    result += s[j + i]
                    if j + numIterations - i < len(s):
                        result += s[j + numIterations - i]
                    j += numIterations
            i += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    # Expected output: "PAHNAPLSIIGYIR"
    print(sol.convert("PAYPALISHIRING", 3))
    # Expected output: "PINALSIGYAHRPI"
    print(sol.convert("PAYPALISHIRING", 4))
    # Expected output: "A"
    print(sol.convert("A", 1))
