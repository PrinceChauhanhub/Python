def knapsack(wt, val, w, n):
    t = [[-1 for i in range(w+1)] for j in range(n+1)]
    # Base Condition
    if n==0 or w==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    
    if wt[n-1]>w:
        # Skip the object completely
        t[n][w] = knapsack(wt, val, w, n-1)
        return t[n][w]
    else:
        t[n][w] = max(val[n-1] + knapsack(wt, val, w-wt[n-1], n-1), knapsack(wt, val, w, n-1))
        return t[n][w]
        
# Driver Code
# Val is profit array
# W is the maximum Capacity

val = [60,100,120]
wt = [10, 20, 30]
w = 50
n = len(val)
print( knapsack(wt,val,w,n))