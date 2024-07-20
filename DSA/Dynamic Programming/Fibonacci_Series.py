# Recursive Approach

# def fib(n):
#     # Base Case Condition
#     if n == 0 or n == 1:
#         return n
    
#     # Recusive calls 
#     else:
#         return fib(n-1) + fib(n-2)

# # result = fib(50)
# # print(result)

# Observation : Using recursion , We are getting an exponential time complexity and when value of n is small, it is giving us the result within few seonds but as the value of n in incresing, time required to generate the results is too much
# Why it is taking too much time when n is quite high?
# bcs the problem is Overlapping subproblem -  Recomputation of same subproblem again and again.

# Solution of overlapping subproblem is Dynamic programming.
# Two approaches using dynamic programming
# 1. Memoization(Top Down Approach)
# 2. Tabulation(Bottom Up Approach)


# Memoization  : using recursion but storing every recursive solution in a data structure.
# Time Complexity : O(n)
# Space Complexity : O(n)

# def fib_topDown(n,memo):
#     if memo[n] is not None:
#         return memo[n]
    
#     # Base case Condition
#     if n == 0 or n == 1:
#         result = n
#     # Recursive Call
#     else:
#         result = fib_topDown(n-1,memo) + fib_topDown(n-2,memo)
#     # Storing function result in array
#     memo[n] = result
#     return result

# def fib_memo(n):
#     # List to store results of every function call
#     memo = [None]*(n+1)
    
#     return fib_topDown (n,memo)

# res = fib_memo(1000)
# print(res)

# At a time when value is 1000 we can see it shows maximum recusion depth exceeded Bcs the limit of the stack which stores the function calls exceeded.stack is not able to handle this number of function call.and also the depth of the recursive tree is very high.
# To overcome the problem we have Tabulation the other approach of dynamic programming

# Tabulation : In this, we get rid of recursion itself. instead recursion we use tabbles to store the values . It is more optimized than memoization.
# Time Complexity : O(n)
# Space Complexity : O(n)

# def fib_bottomUp(n):
#     bottomUp = [None]*(n+1)
#     bottomUp[0] = 0
#     bottomUp[1] = 1
    
#     # No recursive function call
#     for i in range(2,n+1):
#         bottomUp[i] = bottomUp[i-1]+ bottomUp[i-2]
#     return bottomUp[n]

# res = fib_bottomUp(2000)
# print(res)

# by using Tabulation we didn't get the error and also it gives result ver fast.
# here we can't comapre tabulation and memoization based on complexitites. 

# We can more optimize the tabulation where the time time complexity will be  O(1) insted of O(n)
# Highly Optimized solution of problem
def fib_bottomUp(n):
    first = 0
    second = 1

    # No recursive function call
    for i in range(2,n+1):
        nxt = first + second
        first, second = second, nxt
    return nxt

res = fib_bottomUp(7)
print(res)
