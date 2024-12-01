from my_utils import get_input_for_day

WHICH_DAY = 3


def get_number_len(line_index: int, char_index: int, lines: list) -> int:
    number_len = 1
    while True:
        if (
            char_index < len(lines[0]) - 2
            and lines[line_index][char_index + 1].isnumeric()
        ):
            char_index += 1
            number_len += 1
        else:
            break
    return number_len


def find_number_indices(lines: list) -> tuple:
    found_numbers = []
    found_stars = []
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1):
            if lines[i][j] == "*":
                found_stars.append([i, j])
            elif j == 0 and lines[i][j].isnumeric():
                found_numbers.append([i, j, get_number_len(i, j, lines)])
            elif j == 0:
                continue
            elif lines[i][j].isnumeric() and not lines[i][j - 1].isnumeric():
                found_numbers.append([i, j, get_number_len(i, j, lines)])
    return found_numbers, found_stars


def is_adjecent_to_special_char(lines: list, number_det: list) -> bool:
    for i in range(3):
        for j in range(number_det[2] + 2):
            current_line = number_det[0] + i - 1
            current_char = number_det[1] + j - 1
            if (
                # if index out of bounds of lines
                current_line < 0
                or current_line >= len(lines)
                or current_char < 0
                or current_char >= len(lines[0])
                # in the number's line check only one field to the left and one to the right
                or (
                    current_line == number_det[0]
                    and current_char != number_det[1] - 1
                    and current_char != number_det[1] + number_det[2]
                )
                # exclude end of line
                or lines[current_line][current_char] == "\n"
            ):
                continue
            if (
                not lines[current_line][current_char].isnumeric()
                and lines[current_line][current_char] != "."
            ):
                return True
    return False


def get_value_of_number_det(lines: list, number_det: list) -> int:
    print(lines[number_det[0]][number_det[1] : number_det[1] + number_det[2]])
    return int(lines[number_det[0]][number_det[1] : number_det[1] + number_det[2]])


def main():
    score = 0
    lines = get_input_for_day(WHICH_DAY)
    found_numbers, found_stars = find_number_indices(lines)
    for star in found_stars:
        print(star)
    print(len(found_stars))
    exit()
    for number_det in found_numbers:
        if is_adjecent_to_special_char(lines, number_det):
            score += get_value_of_number_det(lines, number_det)

    print(f"Score one is: {score}")


if __name__ == "__main__":
    main()
