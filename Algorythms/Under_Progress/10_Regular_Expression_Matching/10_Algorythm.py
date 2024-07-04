class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        last_cc = ""
        for i in range(len(s)):
            if p == "":
                print("fales0")
                return False
            for cc in p:
                print(cc, p, s[i])
                if s[i] == cc:
                    p = p[p.index(cc) + 1 :]
                    last_cc = cc
                    break
                elif cc == ".":
                    p = p[p.index(cc) + 1 :]
                    last_cc = cc
                    break
                elif cc == "*":
                    if last_cc == ".":
                        if len(p) == 1:
                            return True
                        else:
                            p = p[p.index(cc) + 1 :]
                            last_cc = last_cc
                            break
                    if last_cc != "":
                        print("yo")
                        print(p, cc, last_cc, s[i])
                        while p != "" and i < len(s) and s[i] == last_cc:
                            print("test")
                            i += 1
                            p = p[p.index(cc) + 1 :]
                        p = p[p.index(cc) + 1 :]
                        last_cc = cc
                        i -= 1
                        print(p, cc, last_cc, s[i])
                        print("yo")
                        break
                else:
                    p = p[p.index(cc) + 1 :]
                    last_cc = cc
            if last_cc != cc:
                print("fales1")
                return False

        if len(p) != 0:
            print(p)
            print("fales2")
            return False
        return True


if __name__ == "__main__":
    # Works till #278
    sol = Solution()
    # # Expected result: False
    # print(sol.isMatch("aa", "a"))
    # # Expected result: True
    # print(sol.isMatch("aa", "a*"))
    # # Expected result: True
    # print(sol.isMatch("ab", ".*"))
    # Expected result: True
    print(sol.isMatch("aab", "c*a*b"))
    # # Expected result: False
    # print(sol.isMatch("mississippi", "mis*is*p*."))
    # # Expected result: True
    # print(sol.isMatch("mississippi", "mis*is*ip*."))
    # # Expected result: False
    # print(sol.isMatch("abcd", "d*"))
    # # Expected result: False
    # print(sol.isMatch("ab", ".*c"))
    # # Expected result: False
    # print(sol.isMatch("aaa", "aaaa"))
    # Expected result: False
    print(sol.isMatch("aaa", "ab*a"))
