#!/usr/bin/python3
import sys


def is_safe(row, col, cols, diag1, diag2):
    if col in cols:
        return False
    if (row - col) in diag1:
        return False
    if (row + col) in diag2:
        return False
    return True


def solve(row, n, board, cols, diag1, diag2):
    if row == n:
        print([[r, board[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(row, col, cols, diag1, diag2):
            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            solve(row + 1, n, board, cols, diag1, diag2)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(0, n, board, set(), set(), set())


if __name__ == "__main__":
    main()
