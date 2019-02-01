from board_utils import *

def find_next_knight_positions(number):
    if (number <= 0):
        return []

    next_knight_positions = []

    (current_x, current_y) = find_position_of_number(number)

    motions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    for (m_x, m_y) in motions:
        next_knight_positions.append(find_number_at_position(current_x + m_x, current_y + m_y))

    return sorted(next_knight_positions)


def main():
    number = int(input("Tell me a number: "))
    positions = find_next_knight_positions(number)
    print(positions)

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            exit()
        except:
            pass
