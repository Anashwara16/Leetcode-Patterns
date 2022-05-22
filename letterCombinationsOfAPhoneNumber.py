
# 17. Letter Combinations of a Phone Number


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if len(digits) == 0:
            return []

        result = []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i, currentString):

            if len(currentString) == len(digits):
                result.append(currentString)
                return

            for c in letters[digits[i]]:
                backtrack(i+1, currentString + c)

        backtrack(0, "")

        return result


if __name__ == "__main__":
    digits = "23"
    objectNums = Solution()
    print(objectNums.letterCombinations(digits))
