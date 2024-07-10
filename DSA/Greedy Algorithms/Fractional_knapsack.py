class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(arr,M):
    arr.sort(key = lambda x:(x.profit/x.weight),reverse = True)
    
    for item in arr:
        print(item.profit ,item.weight,item.profit/item.weight)
    maxProfit=0.0
    
    for item in arr:
        if item.weight <= M:
            M-=item.weight
            maxProfit+=item.profit
        else:
            maxProfit+=item.profit * M/item.weight
            break
    return maxProfit

M = 37
arr = [Item(25, 5),Item(75, 10),Item(100, 12),Item(50, 4),Item(45, 7),Item(90, 9),Item(30, 3)]

maxProfit = fractionalKnapsack(arr,M)
print("Maximum profit using greedy algorithm is", maxProfit)