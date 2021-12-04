#!/usr/bin/env python3 -u

def get_diff():
    inc_counts = 0
    with open("input.txt") as input:
        prev_num = int(input.readline())
        cur_num = prev_num
        while cur_num:
            try:
                cur_num = int(input.readline())
            except ValueError:
                break
            else:
                inc_counts += ((cur_num - prev_num) > 0)
                prev_num = cur_num

    print(f"Total Increase counts: {inc_counts}")


if __name__ == '__main__':
    get_diff()