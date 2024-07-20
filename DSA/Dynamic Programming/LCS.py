# Tabulation Approach (DP)
# Time Complexity -> O(m * n)
# Space Complexity -> O(m * n)
 
def LCS(x,y):
    # m - no or rows
    # n - no. of cols
    
    m = len(x)
    n = len(y)
    
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[m][n]

string1 = "BD"
string2 = "ABCD"
print("Length of LCS is ",LCS(string1, string2))