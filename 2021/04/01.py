from typing import Tuple, List


def read_input() -> Tuple[List[int], List[List[List[int]]]]:
    boards = []
    with open("input.txt") as inp:
        rand_nums = list(map(int, inp.readline().split(',')))
        inp.readline()
        while True:
            board = []
            for i in range(5):
                row = list(map(int, inp.readline().split()))
                board.append(row)
            boards.append(board)
            nl = inp.readline()
            if not nl:
                break

    return rand_nums, boards


def check_win(board):
    for row in board:
        if sum(row) == -5:
            return True

    col_sum = [0] * 5
    for i in range(5):
        col_sum[i] = sum(row[i] for row in board)
        if col_sum[i] == -5:
            return True


def sum_board(board):
    return sum(sum(filter(lambda e: e > 0, row)) for row in board)


def win_score(boards: List[List[List[int]]], rand_nums: List[int]):
    for num in rand_nums:
        for board in boards:
            for row in board:
                if num in row:
                    row[row.index(num)] = -1

            win = check_win(board)
            if win:
                return sum_board(board) * num


if __name__ == '__main__':
    rand, boards = read_input()
    print(win_score(boards, rand))
