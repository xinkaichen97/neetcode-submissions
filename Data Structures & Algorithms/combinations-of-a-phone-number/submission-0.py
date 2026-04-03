class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
          
        # number to letter mapping
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        # backtrack function
        def backtrack(idx, comb):
            # return criterion: indices reach the end
            if idx == len(digits):
                res.append(comb)
                return

            # call backtrack with index + 1 and updated letters
            # for each letter in digits, the worst case is 4 possible next letters, so the total path is 4^n
            # and since string concatenation is O(n), total time complexity is O(n * 4^n)
            for letter in mapping[digits[idx]]:
                backtrack(idx + 1, comb + letter)

        # backtrack from index 0 and an empty string
        backtrack(0, "")

        return res