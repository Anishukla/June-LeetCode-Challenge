"""
Name of the problem :- Coin Change 2
"""

A = int(input())
coins = list(map(int, input().split()))
coins = sorted(coins)
L = [[0 for i in range(A+1)] for j in range(len(coins)+1)] 

L[0][0] = 1


for i in range(1, len(coins)+1):
    for j in range(0, A+1):
        val = coins[i-1]
        if j>=val:
            L[i][j] = L[i-1][j]+L[i][j-val]
            
        else:
            L[i][j] = L[i-1][j]
            
print(L[-1][-1])