
def final_pos():
    x = y = 0
    with open("input.txt") as inp:
        while True:
            instr = inp.readline()
            try:
                cmd, val = instr.split()
            except ValueError:
                break
            else:
                if cmd == "forward":
                    x += int(val)
                elif cmd == "down":
                    y += int(val)
                elif cmd == "up":
                    y -= int(val)

        print(f"Final Val: {x * y}")


if __name__ == '__main__':
    final_pos()