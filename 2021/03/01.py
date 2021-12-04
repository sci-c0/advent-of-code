import reprlib


def bin_diag():
    diag_report = []
    counts_1 = []
    with open("input.txt") as inp:
        while True:
            try:
                diag_report.append(list(map(int, inp.readline().split()[0])))
            except IndexError:
                break

    total = len(diag_report)

    for diag in diag_report:
        if not counts_1:
            counts_1 = diag.copy()
            continue
        for i, val in enumerate(diag):
            counts_1[i] += val

    # print(diag_report)
    print(total, counts_1)

    gamma_list = [int(count > total - count) for count in counts_1]
    epsilon_list = [int(count < total - count) for count in counts_1]

    gamma = int(''.join(map(str, gamma_list)), 2)
    epsilon = int(''.join(map(str, epsilon_list)), 2)

    print(f"Power Consumption: {gamma * epsilon}")


if __name__ == '__main__':
    bin_diag()
