import matplotlib.pyplot as plt
from math import sin, cos, pi


ALPHA = -pi/2
ANGLE = pi/4

def draw_branch(x, y, length, alpha, angle, depth):
    if depth == 0:
        return

    x1 = x + length * cos(alpha)
    y1 = y + length * sin(alpha)
    
    plt.plot([x, x1], [y, y1], color='brown')

    draw_branch(x1, y1, length * cos(angle), alpha + angle, angle, depth - 1)
    draw_branch(x1, y1, length * cos(angle), alpha - angle, angle, depth - 1)

if __name__ == "__main__":
    try:
        recursion_level = int(input("\nInput recursion level (only numbers >= 3):--> "))
        plt.figure(figsize=(10, 10))
        plt.title("Pythagoras Tree")
        plt.axis('equal')
        plt.axis('off')

        if recursion_level <= 2:
            raise ValueError
        elif recursion_level > 12:
            answer = input("\nRecursion level is too high, it will take some time, are you sure? (y/n):--> ")
            if answer.lower() != 'y':
                raise ValueError

        draw_branch(0, 0, 1, ALPHA, ANGLE, recursion_level)
        plt.show()
        
    except ValueError:
        print("\nYou need to enter only numbers >= 3, please restart\n")