class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        diagsum=0
        for i in range(n):
            diagsum+=mat[i][i]

        for i in range(n):
            diagsum+=mat[i][n-1-i]

        if n%2==1:
            diagsum-=mat[int(n/2)][int(n/2)]
        return diagsum