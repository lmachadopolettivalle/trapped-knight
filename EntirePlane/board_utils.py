import math

# 1: Position (0, 0)
# (2n+1)^2: Position (n, -n)
# Position (n, n): (2n-1)^2 + 2n
# Position (-n, n): Position (n, n) + 2n = (2n-1)^2 +4n
# Position (-n, -n): Position (-n, n) + 2n = (2n-1)^2 + 6n
# Indeed: Position (n, -n) = Position (-n, -n) + 2n = (2n-1)^2 + 8n = 4n^2-4n+1+8n = (2n+1)^2 as stated above!

# Return coordinates of number in this Cartesian plane:
# Start 1 at (0, 0), wrap around counterclockwise starting to the right
# See https://www.youtube.com/watch?v=RGQe8waGJ4w (Trapped Knight by Numberphile)
def find_position_of_number(number):
    if (number <= 0):
        return None

    # Find largest odd number whose square is smaller than 'number'
    # Equivalent: find largest odd number smaller than sqrt('number')
    root = math.floor(math.sqrt(number))
    largest_odd_smaller = root if (root % 2 == 1) else (root-1)
    n = math.floor((largest_odd_smaller - 1) / 2)
    L = largest_odd_smaller * largest_odd_smaller

    # Number >= largest_odd_smaller**2 (call largest_odd_smaller**2 == L)
    # Position (n, -n): L = (2*n+1)**2
    # Complete difference from L to number by adding to L
    if number < L:
        print(f"This is a messed up system for number {number}")
        return None

    x = n
    y = -n

    # First, move one position to the right
    if number > L:
        L += 1
        x += 1

    # Then, move up, left, down and right
    # You will reach 'number' by the end, or otherwise L is ill-defined
    # as the largest odd smaller than the root of 'number'

    # Up
    for _ in range(largest_odd_smaller):
        if L >= number:
            break
        L += 1
        y += 1

    # Left
    for _ in range(largest_odd_smaller+1):
        if L >= number:
            break
        L += 1
        x -= 1

    # Down
    for _ in range(largest_odd_smaller+1):
        if L >= number:
            break
        L += 1
        y -= 1

    # Right
    for _ in range(largest_odd_smaller):
        if L >= number:
            break
        L += 1
        x += 1


    return (x, y)


def find_number_at_position(x, y):
    # Determine smaller_square and larger_square, two consecutive odd squares
    # such that smaller_square <= number <= larger_square
    n = max(abs(x), abs(y))

    if n == 0:
        return 1

    small = 2*n - 1
    large = 2*n + 1
    smaller_square = small ** 2
    larger_square  = large ** 2

    # smaller_square is at position (n-1, -(n-1))
    L = smaller_square
    x_try = n - 1
    y_try = -x_try

    # First, try one to the right
    L += 1
    x_try += 1
    if (x_try, y_try) == (x, y):
        return L

    # Up
    for _ in range(small):
        if (x_try, y_try) == (x, y):
            return L
        L += 1
        y_try += 1

    # Left
    for _ in range(small + 1):
        if (x_try, y_try) == (x, y):
            return L
        L += 1
        x_try -= 1

    # Down
    for _ in range(small + 1):
        if (x_try, y_try) == (x, y):
            return L
        L += 1
        y_try -= 1

    # Right
    for _ in range(small + 1):
        if (x_try, y_try) == (x, y):
            return L
        L += 1
        x_try += 1

    return L




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
