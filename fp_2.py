import matplotlib.pyplot as plt
from math import sin, cos, pi


ALPHA = -pi/2
ANGLE = pi/4
PI_2 = pi/2

def draw_branch(x, y, length, alpha, angle, depth, counter):
    if depth == 0:
        return
    
    dx = length * sin(alpha)
    dy = length * cos(alpha)

    X, Y = [x], [y]

    x1 = x + dx
    y1 = y - dy
    X.append(x1)
    Y.append(y1)

    x2 = x + dx - dy
    y2 = y - dy - dx
    X.append(x2)
    Y.append(y2)

    x3 = x - dy
    y3 = y - dx
    X.append(x3)
    Y.append(y3)

    x4 = x - dy + length * cos(angle) * sin(alpha - angle)
    y4 = y - dx - length * cos(angle) * cos(alpha - angle)

    col = (1/counter)**0.25
    plt.fill(X, Y, color="Black", alpha = col)

    draw_branch(x4, y4, length * sin(angle), alpha - angle + PI_2, angle, depth - 1, counter + 1)
    draw_branch(x3, y3, length * cos(angle), alpha - angle, angle, depth - 1, counter + 1)
    pass


if __name__ == "__main__":

    try:
        recursion_level = 3
        recursion_level = int(input("\nInput recursion level (only numbers >= 3):--> "))
        plt.title("Classic Pythagoras tree")
        plt.tight_layout()
        plt.axis('equal')
        plt.axis('off')

        if recursion_level <= 2:
            raise ValueError
        elif recursion_level > 12:
            while True:
                answer = input(
                    "\nRecursion level is too high, it will take some time, are you shure? (y/n):--> "
                )
                if answer == "y" or answer == "Y":
                    draw_branch(-1, -1, 1, ALPHA, ANGLE, recursion_level, 1)
                    plt.show()
                    break
                elif answer == "n" or answer == "N":
                    break
        else:
            draw_branch(-1, -1, 1, ALPHA, ANGLE, recursion_level, 1)
            plt.show()
            
    except ValueError:
        print("\nYou need to enter only numbers >= 3, pls restart\n")
