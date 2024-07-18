def jobScheduling(arr,maxDeadline):
    n =len(arr)
    arr.sort(key = lambda x:x[1], reverse = True)
    
    # results shows that job is already occupied on that day or not
    # job stores the actual jobs inside the list
    
    result = [False]*maxDeadline
    job = [-1]*maxDeadline

    for i in range(n):
        for j in range(min(maxDeadline-1,arr[i][2]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                job[j] = arr[i][0]
                break
    
    print("job sequence to get the max profir",job)
# Array contains three columns (Job NUmber , Profit, Deadline)
# COnstraint: Every job needs to be completed before or equal to the given deadline
# Optimization: Maximum Profit
arr = [
    ['J1',55,5],
    ['J2',65,2],
    ['J3',75,7],
    ['J4',60,3],
    ['J5',70,2],
    ['J6',50,1],
    ['J7',85,4],
    ['J8',68,5],
    ['J9',45,3],
]

maxDeadline = 7

jobScheduling(arr,maxDeadline)