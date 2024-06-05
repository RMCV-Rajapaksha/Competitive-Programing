class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        
        for i in range(len(words)):
            if words[i][0]!=s[i] or len(words[i])==0:
                return False
        
        return True