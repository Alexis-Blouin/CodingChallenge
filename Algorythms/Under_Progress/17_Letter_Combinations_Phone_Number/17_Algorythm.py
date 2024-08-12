class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """


if __name__ == "__main__":
    sol = Solution()
    # Expected result: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(sol.letterCombinations("23"))
    # Expected result: []
    print(sol.letterCombinations(""))
    # Expected result: ["a","b","c"]
    print(sol.letterCombinations("2"))
