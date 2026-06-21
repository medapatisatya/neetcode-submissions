class Solution:
    def board_splitter(self, board, bs):
        for hl in board:
            gr = []
            for i in [0,3,6]:
                l = [x for x in hl[i:i+3] if not x == '.']
                s = set(l)
                if len(l) != len(s): return False
                gr.append(s)
            if (gr[0]&gr[1]) or (gr[0]&gr[2]) or (gr[1]&gr[2]): return False
            bs.append(gr)
        return True


    def board_block_verifier(self, l):
        for i in [0,3,6]:
            for j in [0,1,2]:
                if (l[i][j]&l[i+1][j]) or (l[i][j]&l[i+2][j]) or (l[i+1][j]&l[i+2][j]): return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hl, vl = [], []
        board_inverted = list(zip(*board))
        res = self.board_splitter(board, hl) and self.board_splitter(board_inverted, vl)
        if not res: return False
        return self.board_block_verifier(hl) and self.board_block_verifier(vl)

