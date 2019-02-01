import matplotlib.pyplot as plt
from board_utils import *
from knight_utils import *

def plot(x, y):
    NPOINTS = len(x)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    cm = plt.get_cmap("jet")
    ax1.set_prop_cycle(color=[cm(1.*i/(NPOINTS-1)) for i in range(NPOINTS-1)])

    for i in range(NPOINTS-1):
        ax1.plot(x[i:i+2],y[i:i+2])

    plt.plot(x[0], y[0], 'ro', label="Start point (1)")
    plt.plot(x[-1], y[-1], 'bx', label="End point ({0})".format(find_number_at_position(x[-1], y[-1])))

    plt.title("Trapped Knight path in corner of plane", fontsize=16)

    plt.legend()

    plt.savefig("Trapped Knight.png")
    plt.show()

def main():
    start = 1
    visited = [1]
    curr = start

    while True:
        print(curr)
        next_possible = find_next_knight_positions(curr)
        next_actually_possible = [x for x in next_possible if x not in visited]

        if len(next_actually_possible) == 0:
            break

        choice_next = min(next_actually_possible)
        curr = choice_next
        visited.append(choice_next)
    
    positions = [find_position_of_number(num) for num in visited]

    x = [a[0] for a in positions]
    y = [a[1] for a in positions]

    plot(x, y)

if __name__ == "__main__":
    main()
