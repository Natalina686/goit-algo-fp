import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_dice_simulation(num_trials):
    # Словник для підрахунку кількості випадків для кожної суми
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_trials):
        die1 = random.randint(1, 6)  # Кидок першого кубика
        die2 = random.randint(1, 6)  # Кидок другого кубика
        total = die1 + die2  # Сума
        sum_counts[total] += 1  # Збільшуємо лічильник для відповідної суми

    # Обчислення ймовірностей
    probabilities = {s: count / num_trials * 100 for s, count in sum_counts.items()}
    return probabilities

def analytical_probabilities():
    # Аналітичні ймовірності для сум від 2 до 12
    return {
        2: 1/36 * 100,
        3: 2/36 * 100,
        4: 3/36 * 100,
        5: 4/36 * 100,
        6: 5/36 * 100,
        7: 6/36 * 100,
        8: 5/36 * 100,
        9: 4/36 * 100,
        10: 3/36 * 100,
        11: 2/36 * 100,
        12: 1/36 * 100,
    }

def plot_probabilities(monte_carlo_probs, analytical_probs):
    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[s] for s in sums]
    analytical_values = [analytical_probs[s] for s in sums]

    x = np.arange(len(sums))  # Місця для групи стовпців
    width = 0.35  # Ширина стовпців

    fig, ax = plt.subplots()
    bars1 = ax.bar(x - width/2, mc_values, width, label='Метод Монте-Карло', color='blue')
    bars2 = ax.bar(x + width/2, analytical_values, width, label='Аналітичні ймовірності', color='orange')

    # Додавання міток і заголовка
    ax.set_ylabel('Ймовірність (%)')
    ax.set_title('Ймовірності сум при киданні двох кубиків')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()

    plt.show()

# Основна частина програми
num_trials = 1000000
monte_carlo_probs = monte_carlo_dice_simulation(num_trials)
analytical_probs = analytical_probabilities()

# Виведення результатів
print("Ймовірності (Метод Монте-Карло):")
for s in range(2, 13):
    print(f"Сума {s}: {monte_carlo_probs[s]:.2f}%")

print("Аналітичні ймовірності:")
for s in range(2, 13):
    print(f"Сума {s}: {analytical_probs[s]:.2f}%")

# Побудова графіка
plot_probabilities(monte_carlo_probs, analytical_probs)