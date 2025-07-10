class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Create a hash set for col, row and boxes
        # for later use
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for row in range(N):
            for col in range(N):
                value = board[row][col]
                if value == ".":
                    continue
                if value in rows[row]:
                    return False
                rows[row].add(value)
                if value in cols[col]:
                    return False
                cols[col].add(value)
                idx = (row // 3)*3 + col // 3
                if value in boxes[idx]:
                    return False
                boxes[idx].add(value)

        return True
                
        