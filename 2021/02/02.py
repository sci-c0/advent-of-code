
def final_pos_2():
    horiz = depth = aim = 0
    with open("input.txt") as inp:
        while True:
            instr = inp.readline()
            try:
                cmd, val = instr.split()
            except ValueError:
                break
            else:
                if cmd == "forward":
                    horiz += int(val)
                    depth += aim * int(val)
                elif cmd == "down":
                    aim += int(val)
                elif cmd == "up":
                    aim -= int(val)

        print(f"Final Val: {horiz * depth}")


if __name__ == '__main__':
    final_pos_2()