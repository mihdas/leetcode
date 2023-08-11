class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pf=''
        strs.sort()
        print(strs)
        smollest=strs.pop(0)
        len_smollest=len(smollest)
        for j in range(len_smollest):
            for i in strs:
                if i[j]!=smollest[j]:
                    return pf

            pf+=smollest[j]    
            
                    
        return pf
        
            ‚