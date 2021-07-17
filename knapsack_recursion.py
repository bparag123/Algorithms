def knapsack(weight_limit, weights, profit, n):
    if n==0 or weight_limit==0:
        return 0
    else:
        if weights[n-1] > weight_limit:
            #skip current element nd start solving for previous ele
            return knapsack(weight_limit, weights, profit, n-1)
        else:
            #get the solution without selecting current element
            excluding = knapsack(weight_limit, weights, profit, n-1)
            #select current element as a change and recursively find the solution of previous
            including = profit[n-1] + knapsack(weight_limit-weights[n-1], weights, profit, n-1)
            # return max profit
            return max(excluding, including)

weight_limit = 30
weights = [10,20,30]
profit = [60, 100, 120]

print(knapsack(weight_limit, weights, profit, len(weights)))