class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        res = num % 1000
        s += int((num - res) / 1000) * "M"
        num = res

        if len(str(num)) == 3:
            if str(num)[0] == "9":
                s += "CM"
                num -= 900
            elif str(num)[0] == "4":
                s += "CD"
                num -= 400
            else:
                res = num % 500
                s += int((num - res) / 500) * "D"
                num = res
                res = num % 100
                print(res, num)
                s += int((num - res) / 100) * "C"
                num = res

        if len(str(num)) == 2:
            if str(num)[0] == "9":
                s += "XC"
                num -= 90
            elif str(num)[0] == "4":
                s += "XL"
                num -= 40
            else:
                res = num % 50
                s += int((num - res) / 50) * "L"
                num = res
                res = num % 10
                s += int((num - res) / 10) * "X"
                num = res

        if str(num)[0] == "9":
            s += "IX"
            num -= 9
        elif str(num)[0] == "4":
            s += "IV"
            num -= 4
        else:
            res = num % 5
            s += int((num - res) / 5) * "V"
            num = res
            s += num * "I"
        return s


if __name__ == "__main__":
    sol = Solution()
    # Expected result: "MMMDCCXLIX"
    print(sol.intToRoman(3749))
    # Expected result: "LVIII"
    print(sol.intToRoman(58))
    # Expected result: "MCMXCIV"
    print(sol.intToRoman(1994))
    # Expected result: "IV"
    print(sol.intToRoman(4))
