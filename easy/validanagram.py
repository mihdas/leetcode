class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        wrds={}
        for char in s:
            if char not in wrds:
                wrds[char]=1
            else:
                wrds[char]+=1

        for char in t:
            if char not in wrds:
                return False
            else:
                wrds[char]-=1

        for wrd in wrds:
            if wrds[wrd]!=0:
                return False


        return True 
            