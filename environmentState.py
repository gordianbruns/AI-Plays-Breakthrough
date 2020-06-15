''' File:    environmentState.py
 *  Purpose: Represents a state of the game breakthrough
 *
 *  Note: Contains EnvironmentState <class>
 *  Class-functions: getters and setters, some helper functions, display_state, terminal_test
 '''


class EnvironmentState:
    def __init__(self, rows, columns, white_pawns, black_pawns):
        self.ROWS = rows                # int that stores the number of rows
        self.COLUMNS = columns          # int that stores the number of columns
        self.white_pawns = white_pawns  # set of tuples consisting of two numbers
        self.black_pawns = black_pawns  # set of tuples consisting of two numbers
        self.turn = 0                   # if 0, then it is whites turn; if 1, then it is blacks turn
        self.terminal = 0               # if 1, then the state is a terminal state

    def get_rows(self):
        return self.ROWS

    def get_columns(self):
        return self.COLUMNS

    def get_white_pawns(self):
        return self.white_pawns

    def set_white_pawns(self, white_pawns):
        self.white_pawns = white_pawns

    def remove_white_pawn(self, pawn):
        self.white_pawns.remove(pawn)

    def add_white_pawn(self, pawn):
        self.white_pawns.add(pawn)

    def get_black_pawns(self):
        return self.black_pawns

    def set_black_pawns(self, black_pawns):
        self.black_pawns = black_pawns

    def remove_black_pawn(self, pawn):
        self.black_pawns.remove(pawn)

    def add_black_pawn(self, pawn):
        self.black_pawns.add(pawn)

    def get_turn(self):
        return self.turn

    def switch_turn(self):  # called each time a player makes a move
        if self.turn:
            self.turn = 0
        else:
            self.turn = 1

    def get_terminal(self):
        return self.terminal

    def display_state(self):  # displays the current state
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                if (row, column) in self.white_pawns:
                    print("O", end="")
                elif (row, column) in self.black_pawns:
                    print("X", end="")
                else:
                    print(".", end="")
            print()
        print()

    def terminal_test(self):  # terminal test
        for column in range(self.COLUMNS):
            if (self.ROWS - 1, column) in self.white_pawns or len(self.black_pawns) == 0:
                self.terminal = 1  # white won
            if (0, column) in self.black_pawns or len(self.white_pawns) == 0:
                self.terminal = 2  # black won
