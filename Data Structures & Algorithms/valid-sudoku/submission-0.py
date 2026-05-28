class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_counts = [0] * 9
        cols = [[] for _ in range(9)]
        square_counts = [0] * 9
        squares = [[] for _ in range(9)]
        for i in range(9):
            row = board[i]
            row_count = 0
            for j in range(9):
                num = row[j]
                if num != ".":
                    row_count += 1
                    col_counts[j] += 1
                    square_counts[(i // 3) * 3 + (j // 3)] += 1
                cols[j].append(num)
                squares[(i // 3) * 3 + (j // 3)].append(num)
            if len(set(row)) - 1 != row_count:
                print(1, len(set(row)) - 1, row_count)
                return False
        for i in range(9):
            if len(set(cols[i])) - 1 != col_counts[i]:
                print(2, len(set(cols[i])) - 1, col_counts[i])
                return False
            if len(set(squares[i])) - 1 != square_counts[i]:
                print(squares)
                print(square_counts)
                print(3, len(set(squares[i])) - 1, square_counts[i])
                return False
        return True
            