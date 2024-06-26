class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ii = 0
        for i in range(len(p)):
            while i < len(p) and p[i] != s[ii] and p[i] != "." and p[i] != "*":
                i += 1
            if p[i] != s[ii] and p[i] != "." and p[i] != "*":
                return False
            if p[i] == ".":
                i += 1
                continue
            elif p[i] == "*":
                if i == len(p) - 1 and ii == len(s) - 1:
                    return True
                while ii < len(s) and s[ii] == p[i - 1]:
                    print(s[ii], p[i - 1])
                    ii += 1
                if ii == len(s) and i < len(p) - 1:
                    return False
                if p[i + 1] == ".":
                    i += 1
                    if i == len(p) - 1:
                        if ii == len(s) - 1:
                            return True
                        else:
                            return False
            else:
                ii += 1

        if ii == len(s):
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    # Expected result: False
    # print(sol.isMatch("aa", "a"))
    # Expected result: True
    # print(sol.isMatch("aa", "a*"))
    # Expected result: True
    # print(sol.isMatch("ab", ".*"))
    # Expected result: True
    # print(sol.isMatch("aab", "c*a*b"))
    # Expected result: False
    print(sol.isMatch("mississippi", "mis*is*p*."))
    # Expected result: True
    print(sol.isMatch("mississippi", "mis*is*ip*."))
    # Expected result: False
    print(sol.isMatch("abcd", "d*"))
