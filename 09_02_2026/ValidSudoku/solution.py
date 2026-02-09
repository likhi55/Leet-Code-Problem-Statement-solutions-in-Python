class Solution:
    @staticmethod
    def is_valid_sudoku(board):
        for r in board:
            part_row = list(filter(lambda x: x != '.', r))
            if len(part_row) != len(set(part_row)):
                return False
        for i in range(len(board)):
            col = [board[j][i] for j in range(len(board))]
            part_col = list(filter(lambda x: x != '.', col))
            if len(part_col) != len(set(part_col)):
                return False
        for i in range(3):
            for j in range(3):
                block = []
                for m in range(3):
                    for n in range(3):
                        block.append(board[3 * i + m][3 * j + n])
                part_block = list(filter(lambda x: x != '.', block))
                if len(part_block) != len(set(part_block)):
                    return False
        return True