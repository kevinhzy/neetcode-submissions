class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in columns[j]:
                    return False
                columns[j].add(val)
                box = (i//3) * 3 + (j//3)
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
        return True
