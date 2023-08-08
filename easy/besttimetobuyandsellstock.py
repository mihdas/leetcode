class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prf=0
        mn=prices[0]
        for i in range(1,len(prices)):
            mn=min(mn,prices[i])
            prf=max(prf,prices[i]-mn)
            

        return prf