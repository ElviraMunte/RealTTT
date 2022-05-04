

class Game:#hello

    def find_3_in_row(board):
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[0][2]:
                return True
            elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return True
            else:
                return False
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return True


    def __init__(self):
        self.board = [[None]*3,[None]*3,[None]*3]

    def __repr__(self):
        return self.board

    def play(self,row,col,token):
        self.board[row][col] = token
    
    @property
    def winner(self):
        result = self.find_3_in_row(self.board)
        if result == True:
            return "winner"

if __name__ == "__main__":
    pass
