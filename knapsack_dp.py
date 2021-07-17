def knapsack(weight_limit, weights, profit, dp, result):
    for i in range(len(weights)+1):
        for j in range(weight_limit+1):
            if i==0 or j==0:
                pass
            else:
                if weights[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    including = profit[i-1] + dp[i-1][j-weights[i-1]]
                    excluding = dp[i-1][j]
                    dp[i][j] = max(excluding, including)
    row = len(weights)
    col = weight_limit

    temp = dp[row][col]
    while row>0 and col>0:
        if temp == dp[row-1][col]:
            row-=1
        else:
            col -= weights[row-1]
            temp = dp[row-1][col]
            result.append(weights[row-1])
            row -= 1

weight_limit = 89
weights = [11,25,45,88,7]
profit = [1,6,18,22,28]
result = []
dp = [[0 for j in range(weight_limit+1)] for i in range(len(weights)+1)]
knapsack(weight_limit, weights, profit, dp, result)
for i in range(len(weights)+1):
    for j in range(weight_limit+1):
        print(dp[i][j], end=" ")
    print("\n")
print("Maximum Profit is {}".format(dp[len(weights)][weight_limit]))
print("Selected Items are {}".format(result))