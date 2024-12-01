from my_utils import get_input_for_day
import numpy as np

WHICH_DAY = 1


def main():
    lines = get_input_for_day(WHICH_DAY)
    
    do_part1(lines)
    

def do_part2(lines, score):
    print("Part two")

def do_part1(lines):
    print("Part one")
    numbers = np.zeros((len(lines), 2))
    for id, line in enumerate(lines):
        one, two = str(line).strip().split(" ")
        print(one, two)
    


if __name__ == "__main__":
    main()
