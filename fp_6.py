import pandas as pd


class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.profit = calories / cost


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def list_from_dict(items: dict):
    items_list = []
    for item in items:
        items_list.append(Item(item, items[item]["cost"], items[item]["calories"]))

    return items_list

# Greedy approach
def greedy_algorithm(items, budget):
    items_list = list_from_dict(items)
    items_list.sort(key=lambda x: x.profit, reverse=True)

    chosen_items = []
    total_calories = 0
    for item in items_list:
        if budget >= item.cost:
            budget -= item.cost
            total_calories += item.calories
            chosen_items.append(item.name)

    return total_calories, budget, chosen_items

# Dynamic Programming approach
def dynamic_programming(items, budget):
    items_list = list_from_dict(items)
    items_names = []
    items_costs = []
    items_calories = []
    for i in items_list:
        items_names.append(i.name)
        items_costs.append(i.cost)
        items_calories.append(i.calories)

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    chosen_items = []
    temp_budget = 0
    n = len(items_calories)

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if items_costs[i - 1] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], items_calories[i - 1] + dp_table[i - 1][j - items_costs[i - 1]])

    j = budget
    for i in range(n, 0, -1):
        if dp_table[i][j] != dp_table[i - 1][j]:
            chosen_items.append(items_names[i-1])
            temp_budget += items_costs[i-1]
            j -= items_costs[i - 1]

    return dp_table[n][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    print("\nBudget", budget)
    for i in items:
        print(i, items[i])

    print("\nGreedy result (by best ratio):", greedy_algorithm(items, budget))
    print("\nDynamic Programming result (by calories):", dynamic_programming(items, budget), "\n")
