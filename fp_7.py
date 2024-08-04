import random
import matplotlib.pyplot as plt
import math
import pandas as pd


random.seed(1234)

def simulate_dice_rolls(num_rolls):
    sum_list = [0 for _ in range(0, 12)]
    probabilities = {}

    for _ in range(num_rolls):
        sum = int(random.uniform(1, 7))
        sum += int(random.uniform(1, 7))
        sum_list[sum-1] += 1

    for i in range(1, 12):
        probabilities[i+1] = sum_list[i] / num_rolls

    print(f"\nAfter {num_rolls} rolls:")
    for key in probabilities:
        print(f"{key}: {probabilities[key]*100:.2f}")
    return probabilities

def plot_probabilities(probabilities, accuracy):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title(f'Ймовірність суми чисел на двох кубиках при {accuracy} кидках')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)
        plot_probabilities(probabilities, accuracy)
