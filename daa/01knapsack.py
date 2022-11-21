itemWorth = [60, 70, 80]
itemWeight = [10, 20, 30]
sackCapacity = 50
n = len(itemWorth)
dp_table = [[-1 for i in range(sackCapacity+1)] for j in range(n+1)]

def knapsack(itemWorth, itemWeight, sackCapacity, n):
    if sackCapacity == 0 or n == 0:
        return 0
    if dp_table[n][sackCapacity] != -1:
        return dp_table[n][sackCapacity]

    if sackCapacity >= itemWeight[n-1]:
        dp_table[n][sackCapacity] = max(itemWorth[n-1] + knapsack(itemWorth, itemWeight, sackCapacity - itemWeight[n-1], n-1), knapsack(itemWorth, itemWeight, sackCapacity, n-1))
        return dp_table[n][sackCapacity]
    else:
        dp_table[n][sackCapacity] = knapsack(itemWorth, itemWeight, sackCapacity, n-1)
        return dp_table[n][sackCapacity]


print(knapsack(itemWorth, itemWeight, sackCapacity, n))
