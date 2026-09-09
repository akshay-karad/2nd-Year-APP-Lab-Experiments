# Experiment 6
# 0/1 Knapsack using Bottom-Up and Top-Down DP


# Bottom-Up Approach
def knapsack_bottom_up(values, weights, W):
    n = len(values)

    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Top-Down Approach (Memoization)
def knapsack_top_down(values, weights, n, W, memo):

    if n == 0 or W == 0:
        return 0

    if memo[n][W] != -1:
        return memo[n][W]

    if weights[n - 1] <= W:
        memo[n][W] = max(
            values[n - 1] + knapsack_top_down(
                values, weights, n - 1,
                W - weights[n - 1], memo
            ),
            knapsack_top_down(
                values, weights, n - 1, W, memo
            )
        )
    else:
        memo[n][W] = knapsack_top_down(
            values, weights, n - 1, W, memo
        )

    return memo[n][W]


# Example
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

n = len(values)

# Bottom-Up result
bottom_up_result = knapsack_bottom_up(values, weights, W)

# Top-Down result
memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
top_down_result = knapsack_top_down(values, weights, n, W, memo)

print("Values:", values)
print("Weights:", weights)
print("Capacity:", W)

print("\nBottom-Up Maximum Value:", bottom_up_result)
print("Top-Down Maximum Value:", top_down_result)
