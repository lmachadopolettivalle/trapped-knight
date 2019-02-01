import math

# Bottom right of the plane, with 1 placed at (1, -1)
# 1: Position (1, -1)
# nth triangular number: Position (1, -n)

def find_nth_triangular_number(n):
    if n <= 0:
        return None

    return round(n * (n + 1) / 2)

# Return coordinates of number in this 1/4 of a Cartesian plane:
# Start 1 at (1, -1), with triangular numbers on the vertical x = 1
# See https://www.youtube.com/watch?v=RGQe8waGJ4w (Trapped Knight by Numberphile)
def find_position_of_number(number):
    if (number < 1):
        return None

    # Find largest triangular number smaller than 'number'
    # We want 1/2 * (n**2 + n) <= number, i.e.
    # n**2 + n - 2*number <= 0
    # Positive root of this: (-1 + sqrt(1 + 8*number))/2
    # Hence want n = floor(positive root)
    n = math.floor(0.5 * (-1 + math.sqrt(1 + 8 * number)))
    largest_triangular_smaller = find_nth_triangular_number(n)
    L = largest_triangular_smaller

    # Position of L: (1, -n)
    if number < L:
        print(f"This is a messed up system for number {number}")
        return None

    x = 1
    y = -n

    # First, check if number is triangular
    if number == L:
        return (x, y)

    # If not, go to (n+1, -1) (corresponding to L+1) and keep doing
    # x -= 1
    # y -= 1
    # L += 1
    # You will reach 'number' by the end, or otherwise L is ill-defined
    # as the largest triangular smaller than 'number'

    x = n + 1
    y = -1
    L += 1

    while L < number:
        x -= 1
        y -= 1
        L += 1

    return (x, y)


def find_number_at_position(x, y):
    # Note that along a diagonal, (x - y) is constant
    # Find the triangular number immediately above the number at (x, y)
    # The difference between the x values (for triangular, it is 1) tells which number it is
    n = -1 * (1 - (x - y))
    larger_triangular = find_nth_triangular_number(n)

    number = larger_triangular - (x - 1)
    
    return number


def main():
    #number = int(input("Tell me a number: "))
    #position = find_position_of_number(number)
    #if position is not None:
    #    print(position)

    x = int(input("Tell me a x: "))
    y = int(input("Tell me a y: "))
    number = find_number_at_position(x, y)
    print(number)

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            exit()
        except:
            pass
