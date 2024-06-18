class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        if x_str[0] == "-":
            x_str = "-" + x_str[:0:-1]
        else:
            x_str = x_str[::-1]
        return int(x_str) if -(2**31) <= int(x_str) <= 2**31 - 1 else 0


if __name__ == "__main__":
    sol = Solution()
    # Expected output: 321
    print(sol.reverse(123))
    # Expected output: -321
    print(sol.reverse(-123))
    # Expected output: 21
    print(sol.reverse(120))
