# https://leetcode.com/problems/word-break-ii/description/
class Solution:
    result = []
    wordDict = None
    def main(self, text, subTexts): 
        if text == "":
            self.result.append(" ".join(subTexts))
            return
        for word in self.wordDict:
            if text.find(word) == 0:
                copySubTexts = deepcopy(subTexts)
                copySubTexts.append(word)
                subText = deepcopy(text[len(word):])
                self.main(subText, copySubTexts)


    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.result = []
        self.wordDict = wordDict
        self.main(s, []) 
        return self.result