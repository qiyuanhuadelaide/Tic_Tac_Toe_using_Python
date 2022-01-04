"""
Tic Tac Toe Simulation Starter Code
"""
import random



class TicTacToeSim:

    # Part 1
    def __init__(self):
        """
        Create the constructor of game class, initialize the simulation, and set up board as a 2D list, turn to player 1, and ai to false
        :param board: to record the board
        :param AI: check whether is human-computer game or not
        :param turn: user turn
        :param AIturn: computer turn
        :param times: how many times put chess down
        """
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  
        self.AI = False
        self.turn = 1
        self.AIturn = 1
        if self.AI and self.turn == 1:
            self.AIturn = 2
        self.times = 0
        # self.step = [(0, 0), (1, 1), (0, 1), (0, 2), (2, 0), (1, 0), (1, 2), (2, 2), (2, 1)]

    def change_turn(self):
        # Change turn to other player
        if self.times == 16:
            return
        if self.AI:
            print("It is Ai's turn.")
            self.smart_move()
            self.print_board()
            return
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        return


    def play_game(self):
        print("Would you like to play against an AI? True/False:", end='')
        # self.settings()
        flag = input()
        if flag == "True":
            self.AI = True
            print("Would you like to be player 1 or 2? 1/2:", end='')
            user = input()
            if user == "1":
                self.turn = 1
                self.AIturn = 2
            elif user == "2":
                self.turn = 2
                self.AIturn = 1
        elif flag == "False":
            self.AI = False

        # This is the driver method for the simulation
        if self.AI and self.turn == 2:
            self.smart_move()
            self.print_board()
        while True:
            f = self.check_winner()
            if f == 0:
                self.take_turn(player=self.turn)
                self.change_turn()
            elif f == -1:
                print("this is a draw!")
                break
            else:  # 1，2
                if self.AIturn == f and self.AI:
                    print("AI win this game!")
                    self.print_board()
                    break
                else:
                    print("user: %d win this game!" % f)
                    self.print_board()
                    break
                break

        return

    # Part 2
    def print_board(self):
        # Print the state of the board using X (player 1) and O (player 2)
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print(self.board[3])
        # print("time = %d" % self.times)
        return

    # Part 3
    def get_move(self):
        # Get input from user asking for their move as a tuple
        print("What move would you like to make?")
        print("Row:", end='')
        row = int(input())
        # row = self.step[self.times][0]

        print("Column:", end='')
        col = int(input())
        # col = self.step[self.times][1]
        return row, col

    # Part 4
    def take_turn(self, player):
        # This is the driver method for a players turn
        print("It is Player %d's turn." % self.turn)
        row, col = self.get_move()
        l = self.get_available_squares()
        # while (row, col) not in l:
        #     # print("This area is occupied!")
        #     row, col = self.get_move()
        if (row, col) in l:
            self.make_move(move=(row, col), player=self.turn)
        self.print_board()
        return

    def get_available_squares(self):
        # Get a list of available squares as tuples (row,col)
        l = []
        for i in range(0, 4):
            for j in range(0, 4):
                if self.board[i][j] == 0:
                    l.append((i, j))
        return l

    def make_move(self, move, player):
        self.board[move[0]][move[1]] = player
        self.times += 1
        return

    # Part 5
    def check_winner(self):
        # Return the player who won 0 if nobody has won, and -1 if it is a draw
        # ways to win horizontally
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != 0:
                return self.board[i][0]
            if self.board[i][3] == self.board[i][1] and self.board[i][3] == self.board[i][2] and self.board[i][3] != 0:
                return self.board[i][3]
        # ways to win vertically
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != 0:
                return self.board[0][i]
            if self.board[3][i] == self.board[1][i] and self.board[3][i] == self.board[2][i] and self.board[3][i] != 0:
                return self.board[3][i]
        # ways to win diagonally
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != 0:
            return self.board[0][0]
        if self.board[3][3] == self.board[1][1] and self.board[3][3] == self.board[2][2] and self.board[3][3] != 0:
            return self.board[3][3]
        if self.board[0][3] == self.board[2][1] and self.board[1][2] == self.board[0][3] and self.board[0][3] != 0:
            return self.board[0][3]
        if self.board[3][0] == self.board[2][1] and self.board[1][2] == self.board[3][0] and self.board[3][0] != 0:
            return self.board[3][0]

        # when the board is full
        if self.times >= 16:
            return -1
        return 0

    # Part 6
    def random_move(self):
        # Choose a random move from available moves

        l = self.get_available_squares()
        Length = len(l)
        index = random.randint(0, Length - 1)
        self.make_move(l[index], self.AIturn)
        return l[index][0], l[index][1]

    # Part 7
    def winning_move(self, player):
        # Find a winning move for a player
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] == player and 0 == self.board[i][2]:# 0,1
                return i, 2
            elif self.board[i][0] == self.board[i][2] == player and 0 == self.board[i][1]:# 0,2
                return i, 1
            elif self.board[i][1] == self.board[i][2] == player and self.board[i][0] == 0:# 1,2
                return i, 0
            elif self.board[i][1] == self.board[i][2] == player and self.board[i][3] == 0:# 1,2
                return i, 3
            elif self.board[i][1] == self.board[i][3] == player and self.board[i][2] == 0:# 1,3
                return i, 2
            elif self.board[i][3] == self.board[i][2] == player and self.board[i][1] == 0:# 2,3
                return i, 1
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] == player and 0 == self.board[2][i]:# 0,1
                return 2, i
            elif self.board[0][i] == self.board[2][i] == player and 0 == self.board[1][i]:# 0,2
                return 1, i
            elif self.board[1][i] == self.board[2][i] == player and self.board[0][i] == 0:# 1,2
                return 0, i
            elif self.board[1][i] == self.board[2][i] == player and self.board[3][i] == 0:# 1,2
                return 3, i
            elif self.board[1][i] == self.board[3][i] == player and self.board[2][i] == 0:# 1,3
                return 2, i
            elif self.board[2][i] == self.board[3][i] == player and self.board[1][i] == 0:# 2,3
                return 1, i

        # if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
        #     return self.board[0][0]
        if self.board[0][0] == self.board[1][1] == player and 0 == self.board[2][2]:
            return 2, 2
        elif self.board[0][0] == self.board[2][2] == player and 0 == self.board[1][1]:
            return 1, 1
        elif self.board[1][1] == self.board[2][2] == player and self.board[0][0] == 0:
            return 0, 0
        elif self.board[1][1] == self.board[2][2] == player and self.board[3][3] == 0:
            return 3, 3
        elif self.board[1][1] == self.board[3][3] == player and self.board[2][2] == 0:
            return 2, 2
        elif self.board[2][2] == self.board[3][3] == player and self.board[1][1] == 0:
            return 1, 1

        if self.board[0][3] == self.board[1][2] == player and 0 == self.board[2][1]:
            return 2, 1
        elif self.board[0][3] == self.board[2][1] == player and 0 == self.board[1][2]:
            return 1, 2
        elif self.board[1][2] == self.board[2][1] == player and self.board[0][3] == 0:
            return 0, 3
        elif self.board[1][2] == self.board[2][1] == player and self.board[3][0] == 0:
            return 3, 0
        elif self.board[1][2] == self.board[3][0] == player and self.board[2][1] == 0:
            return 2, 1
        elif self.board[2][1] == self.board[3][0] == player and self.board[1][2] == 0:
            return 1, 2

        return None

    def threat_to_lose(self):
        # Run winning_move from other perspective
        return self.winning_move(self.turn)

    def smart_move(self):
        # If there is a winning move, win
        # If there is a threat to lose, block
        # Make random move
        w_move = self.winning_move(player=self.AIturn)
        if w_move is not None:
            self.make_move(move=w_move, player=self.AIturn)
            return w_move
        else:
            l_move = self.threat_to_lose()
            if l_move is not None:
                self.make_move(move=l_move, player=self.AIturn)
                return l_move
            else:
                r_move = self.random_move()
                return r_move

    # def settings(self):
    #     flag = input()
    #     if flag == "True":
    #         self.AI = True
    #         user = input()
    #         if user == "1":
    #             self.turn = 1
    #         elif user == "2":
    #             self.turn = 2
    #     elif flag == "False":
    #         self.AI = False


# print("Would you like to play against an AI? True/False:", end='')
# flag = False
# user = 1
# step = [(0, 0), (1, 1), (0, 1), (0, 2), (2, 0), (1, 0), (1, 2), (2, 2), (2, 1)]
# if input() == "True":
#    flag = True
#    print("Would you like to be player 1 or 2? 1/2:", end='')
#    if input() == "2":
#        user = 2
# sim = TicTacToeSim()
# sim.play_game()
