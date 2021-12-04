#!/usr/bin/env python3 -u

def get_diff():
    inc_counts = 0
    with open("input.txt") as inp:
        prev_nums = []
        for i in range(3):
            prev_nums.append(int(inp.readline()))
        cur_nums = prev_nums.copy()
        cur_nums.pop(0)
        while True:
            try:
                cur_num = int(inp.readline())
            except ValueError:
                break
            else:
                cur_nums.append(cur_num)
                inc_counts += (sum(cur_nums) - sum(prev_nums) > 0)
                prev_nums.pop(0)
                prev_nums.append(cur_num)
                cur_nums.pop(0)

    print(f"Total Increase counts: {inc_counts}")


if __name__ == '__main__':
    get_diff()