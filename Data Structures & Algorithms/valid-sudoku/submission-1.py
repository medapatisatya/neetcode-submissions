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
        # hl, vl = [], []
        # board_inverted = list(zip(*board))
        # res = self.board_splitter(board, hl) and self.board_splitter(board_inverted, vl)
        # if not res: return False
        # return self.board_block_verifier(hl) and self.board_block_verifier(vl)

        # using r,c,b list of sets.
        # r,c,b = defaultdict(set), defaultdict(set), defaultdict(set)
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == '.': continue
        #         if board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in b[(i//3)*3+(j//3)]:
        #             return False
        #         else:
        #             r[i].add(board[i][j])
        #             c[j].add(board[i][j])
        #             b[(i//3)*3+(j//3)].add(board[i][j]) 
        # return True

        # using r,c,b list of bit masks.
        r,c,b = [0]*9, [0]*9, [0]*9
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                num = int(board[i][j])-1
                if (r[i] & 1 << num) or (c[j] & 1 << num) or (b[i//3*3+j//3] & 1 << num): return False
                r[i] |= 1 << num
                c[j] |= 1 << num
                b[i//3*3+j//3] |= 1 << num
        return True
