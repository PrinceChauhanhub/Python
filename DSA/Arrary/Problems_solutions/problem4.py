#Best time to buy and sell stock (leetcode - 121 )
#Time Complexity : O(n)

def FindMaxProfit(price):
    minPrice=float('inf')
    maxProfit=0
    
    for i in range(len(price)):
        if price[i]< minPrice:
                minPrice=price[i]
        elif price[i] - minPrice >maxProfit:
                maxProfit=price[i] - minPrice
    return maxProfit
    

price = [7,4,5,3,6,16]  
MaxProfit=FindMaxProfit(price)

print("THe Maximum profit of buying and selling stock is ",MaxProfit)