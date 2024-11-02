def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості та сортуємо за цим критерієм
    items_ratio = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, details in items_ratio:
        if details['cost'] <= budget:
            selected_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    selected_items = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    items_list = list(items.items())

    for i in range(1, n + 1):
        item_name, item_details = items_list[i - 1]
        cost = item_details['cost']
        calories = item_details['calories']
        
        for w in range(budget + 1):
            if cost <= w:
                # Вибір між включенням або виключенням поточного елемента
                if dp[i - 1][w] < dp[i - 1][w - cost] + calories:
                    dp[i][w] = dp[i - 1][w - cost] + calories
                    selected_items[i][w] = selected_items[i - 1][w - cost] + [item_name]
                else:
                    dp[i][w] = dp[i - 1][w]
                    selected_items[i][w] = selected_items[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                selected_items[i][w] = selected_items[i - 1][w]

    return selected_items[n][budget], dp[n][budget]

# Приклад
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик жадібного алгоритму
greedy_selection, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_selection)
print("Сумарна калорійність:", greedy_calories)

# Виклик динамічного програмування
dp_selection, dp_calories = dynamic_programming(items, budget)
print("Динамічне програмування:")
print("Вибрані страви:", dp_selection)
print("Сумарна калорійність:", dp_calories)