def knapsack(weight_limit, weights, profit, dp):
    for i in range(len(weights)+1):
        for j in range(weight_limit+1):
            if i==0 or j==0:
                pass
            else:
                if weights[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], profit[i-1] + dp[i-1][weight_limit-weights[i-1]])


weight_limit = 5
weights = [2,3,4,5]
profit = [3,4,5,6]

dp = [[0 for j in range(weight_limit+1)] for i in range(len(weights)+1)]
knapsack(weight_limit, weights, profit, dp)
for i in range(len(weights)+1):
    for j in range(weight_limit+1):
        print(dp[i][j], end=" ")
    print("\n")
print("Profit is {}".format(dp[len(weights)][weight_limit]))