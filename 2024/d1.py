from my_utils import get_input_for_day
import numpy as np

WHICH_DAY = 1


def main():
    lines = get_input_for_day(WHICH_DAY)
    
    do_part1(lines)
    do_part2(lines)

def get_numbers_from_lines(lines):
    numbers = np.zeros((len(lines), 2))
    for id, line in enumerate(lines):
        one, two = str(line).strip().split("   ")
        numbers[id] = (int(one), int(two))
    return numbers 
    
def do_part2(lines):
    print("Part two")
    numbers = get_numbers_from_lines(lines)
    unique_in_left = np.unique(numbers[:, 0])
    occurences_in_right = np.zeros((len(unique_in_left), 2))
    for id, number in enumerate(unique_in_left):
        occurences_in_right[id] = (number, np.count_nonzero(numbers[:, 1] == number))
    multiply = occurences_in_right[:, 0] * occurences_in_right[:, 1]
    print(np.sum(multiply))    

def do_part1(lines):
    print("Part one")
    numbers = get_numbers_from_lines(lines)   
    diff = np.abs(np.sort(numbers[:, 0]) - np.sort(numbers[:, 1]))
    print("Answer is: "+ str(np.sum(diff)))

if __name__ == "__main__":
    main()
