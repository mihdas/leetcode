class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        k=0
        res=""
        for i in range(min(l1,l2)):
            res=res+word1[i]
            res=res+word2[i]
            k+=1

        if (l1>l2):
            res=res+word1[k:]
        
        else:
            res=res+word2[k:]
        return res
