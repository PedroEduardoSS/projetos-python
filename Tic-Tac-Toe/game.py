class tic_tac_toe:
    def __init__(self):
        self.board = self.game_loop()

    def game_loop(self):
        self.winner = False
        self.matrix_board = [" "," "," "," "," "," "," "," "," "]
        print(f"{self.matrix_board[0]}|{self.matrix_board[1]}|{self.matrix_board[2]}\n{self.matrix_board[3]}|{self.matrix_board[4]}|{self.matrix_board[5]}\n{self.matrix_board[6]}|{self.matrix_board[7]}|{self.matrix_board[8]}")
        while self.winner == False:
            self.x_player(self.matrix_board)
            self.check_x_won(self.matrix_board)
            self.o_player(self.matrix_board)
            self.check_o_won(self.matrix_board)

    def x_player(self, board):
        self.board = board
        self.mark_x = "X"
        self.position_x = int(input("Position(X): "))
        for pos in range(0, 9):
            if self.position_x == pos:
                self.board[self.position_x] = self.mark_x
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}\n{self.board[3]}|{self.board[4]}|{self.board[5]}\n{self.board[6]}|{self.board[7]}|{self.board[8]}")
    
    def o_player(self, board):
        self.board = board
        self.mark_o = "O"
        self.position_o = int(input("Position(O): "))
        for pos in range(0, 9):
            if self.position_o == pos:
                self.board[self.position_o] = self.mark_o
        print(f"{self.board[0]}|{self.board[1]}|{self.board[2]}\n{self.board[3]}|{self.board[4]}|{self.board[5]}\n{self.board[6]}|{self.board[7]}|{self.board[8]}")
            
    def check_x_won(self, board):
        self.board = board
        if self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X":
            self.winner = True
            print("X won!")
        elif self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X":
            self.winner = True
            print("X won!")
        elif self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X":
            self.winner = True
            print("X won!")
        elif self.board[0] == "X" and self.board[3] == "X" and self.board[6] == "X":
            self.winner = True
            print("X won!")
        elif self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X":
            self.winner = True
            print("X won!")
        elif self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X":
            self.winner = True
            print("X won!")
        elif self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X":
            self.winner = True
            print("X won!")
        elif self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X":
            self.winner = True
            print("X won!")
        else:
            pass
    
    def check_o_won(self, board):
        self.board = board
        if self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O":
            self.winner = True
            print("O won!")
        elif self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O":
            self.winner = True
            print("O won!")
        elif self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O":
            self.winner = True
            print("O won!")
        elif self.board[0] == "O" and self.board[3] == "O" and self.board[6] == "O":
            self.winner = True
            print("O won!")
        elif self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O":
            self.winner = True
            print("O won!")
        elif self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O":
            self.winner = True
            print("O won!")
        elif self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O":
            self.winner = True
            print("O won!")
        elif self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O":
            self.winner = True
            print("O won!")
        else:
            pass