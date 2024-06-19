class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ii = 0
        for i in range(len(s)):
            if ii < len(p):
                if s[i] != p[ii] and p[ii] != "." and p[ii] != "*":
                    while ii < len(p) and s[i] not in [p[ii], ".", "*"]:
                        ii += 1
                    if ii == len(p):
                        print("1")
                        return False
                elif s[i] == p[ii] or p[ii] == ".":
                    ii += 1
                elif p[ii] == "*":
                    ii += 1
                    while ii < len(p) and p[ii] == ".":
                        ii += 1
                        i += 1
                    if ii == len(p) and i < len(s):
                        return True
                    elif ii == 0:
                        print("2")
                        return False
                    print(s[i], p[ii])
                    while i < len(s) and s[i] != p[ii]:
                        i += 1
                    if i == len(s):
                        print("3")
                        return False
            else:
                print("4")
                return False
        print(ii)
        if ii < len(p) and p[ii] != "*" and p[ii] != ".":
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    # Expected result: False
    print(sol.isMatch("aa", "a"))
    # Expected result: True
    print(sol.isMatch("aa", "a*"))
    # Expected result: True
    print(sol.isMatch("ab", ".*"))
    # Expected result: True
    print(sol.isMatch("aab", "c*a*b"))  # Fails
