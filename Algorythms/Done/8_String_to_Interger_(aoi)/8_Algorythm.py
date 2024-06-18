class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            result = ""
            while s[0] == " ":
                s = s[1:]
                if not s:
                    return 0
            if s[0] == "-":
                result += "-"
                s = s[1:]
            elif s[0] == "+":
                s = s[1:]
            while s[0].isdigit():
                result += s[0]
                s = s[1:]
                if not s:
                    break

            result = int(result)
            if result < -(2**31):
                return -(2**31)
            elif result > 2**31 - 1:
                return 2**31 - 1
            return result
        except:
            return 0


if __name__ == "__main__":
    # Expected output: 42
    print(Solution().myAtoi("42"))
    # Expected output: -42
    print(Solution().myAtoi("   -42"))
    # Expected output: 1337
    print(Solution().myAtoi("1337c0d3"))
    # Expected output: 0
    print(Solution().myAtoi("0-1"))
    # Expected output: 0
    print(Solution().myAtoi("words and 987"))
