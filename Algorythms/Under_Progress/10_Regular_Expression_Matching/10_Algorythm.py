class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # last_c = ""
        last_cc = ""
        for i in range(len(s)):
            if p == "":
                return False
            for cc in p:
                print(s[i], cc, p)
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
                        return True
                    if last_cc != "":
                        while p != "" and s[i] == last_cc:
                            i += 1
                        p = p[p.index(cc) + 1 :]
                        break

                        # for c in p:
                        #     if s == "":
                        #         return True
                        #     for cc in s:
                        #         print(c, cc, s)
                        #         if c == cc:
                        #             s = s[s.index(cc) + 1 :]
                        #             last_c = c
                        #             break
                        #         elif c == ".":
                        #             s = s[s.index(cc) + 1 :]
                        #             last_c = c
                        #             break
                        #         elif c == "*":
                        #             if last_c == ".":
                        #                 return True
                        #             if last_c != "":
                        #                 # print(last_c, s)
                        #                 while s != "" and s[0] == last_c:
                        #                     s = s[s.index(s[0]) + 1 :]
                        # break
            if last_cc == cc:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    # # Expected result: False
    # print(sol.isMatch("aa", "a"))
    # # Expected result: True
    # print(sol.isMatch("aa", "a*"))
    # # Expected result: True
    # print(sol.isMatch("ab", ".*"))
    # # Expected result: True
    # print(sol.isMatch("aab", "c*a*b"))
    # Expected result: False
    print(sol.isMatch("mississippi", "mis*is*p*."))
    # Expected result: True
    print(sol.isMatch("mississippi", "mis*is*ip*."))
    # Expected result: False
    print(sol.isMatch("abcd", "d*"))
