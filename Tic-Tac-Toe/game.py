class tic_tac_toe:
    def __init__(self):
        self.board = self.make_board()
        self.winner = None

    def make_board(self):
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.p5 = None
        self.p6 = None
        self.p7 = None
        self.p8 = None
        self.p9 = None
        print(f"{self.p1}|{self.p2}|{self.p3}\n{self.p4}|{self.p5}|{self.p6}\n{self.p7}|{self.p8}|{self.p9}")

    def x_player(self):
        self.position_x = int(input("Position: "))    

    def x_player(self):
        self.position_x = int(input("Position: "))