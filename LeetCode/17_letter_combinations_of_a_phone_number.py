# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapData = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }

        result = []
        # digits = "23"

        groups = []
        groups1 = list(combinations_with_replacement(range(4), len(digits)))
        for group1 in groups1:  
            for group2 in list(permutations(group1)):
                groups.append(group2)
        groups = set(groups)

        for group in groups:
            text = ""
            for i in range(len(digits)):
                if group[i] >= len(mapData[digits[i]]):
                    text = ""
                    break
                text += mapData[digits[i]][group[i]]
            if text != "":
                result.append(text)

        print(result)
        return result