import abc
import tkinter as tk
from PIL import Image, ImageTk

#################################################
#               Initial data                    #
#################################################
height = 70
width = 70
root = tk.Tk()
root.title("Chess")
my_image = ImageTk.PhotoImage(Image.open("pictures/Test.png"))
none_image = ImageTk.PhotoImage(Image.open("pictures/pices/none.png"))
pawn_image_black = ImageTk.PhotoImage(Image.open("pictures/pices/black_pawn.png"))
pawn_image_white = ImageTk.PhotoImage(Image.open("pictures/pices/white_pawn.png"))
king_image_white = ImageTk.PhotoImage(Image.open("pictures/pices/white_king.png"))
king_image_black =ImageTk.PhotoImage(Image.open("pictures/pices/black_king.png"))
board_column = "abcdefgh"
board_data = dict()


#################################################
#               Creating board                  #
#################################################
class Board:
    def __init__(self):
        self.board_data = dict()
        self.board_legend = dict()
        self.my_image = ""
        ###############
        #   legends
        ##############
        for i in board_column:
            self.board_legend[i] = tk.Label(root, text=i).grid(row=0, column=board_column.index(i) + 1)
            self.board_legend[board_column.index(i)] = tk.Label(root, text=9 - (board_column.index(i) + 1)).grid(
                row=board_column.index(i) + 1, column=0)
            self.board_legend[f"{i}2"] = tk.Label(root, text=i).grid(row=9, column=board_column.index(i) + 1)
            self.board_legend[f"{board_column.index(i)}D"] = tk.Label(root, text=9 - (board_column.index(i) + 1)).grid(
                row=board_column.index(i) + 1, column=9)

        #########################
        #   loading board data
        #########################
        for row in range(1, 9):
            for column in board_column:
                if row % 2 == 0:
                    color = "gray" if board_column.index(column) % 2 == 0 else "white"
                else:
                    color = "white" if board_column.index(column) % 2 == 0 else "gray"
                data = self.contributor(row, column)

                # print(my_image)
                # print(data[1])
                #img=data[1]
                self.board_data[f"{column}{9 - row}"] = [
                    tk.Button(root, height=height, width=width, bg=color, image=data[1],
                              command=lambda slot=f"{column}{9 - row}": self.select(slot)), data[0]]
                self.board_data[f"{column}{9 - row}"][0].grid(row=row, column=board_column.index(column) + 1)

    def select(self, slot):
        self.board_data[slot][0].configure(bg="red")

    def contributor(self, row, column):
        if row in [3, 4, 5, 6]:
            return [None, none_image]
        elif row == 7:
            return [None, pawn_image_white]
        elif row == 2:
            return [None, pawn_image_black]
        elif row ==8:
            return [None, king_image_white]
        elif row ==1:
            return [None, king_image_black]


##################################
#   Defining Pieces
##################################

class Piece:
    def __init__(self, white, location, range=9):
        self.white = white
        self.location = location
        self.activated = True
        self.range = range
        self.possible_movements_list = list()
        self.image = ""
        # ImageTk.PhotoImage(Image.open("pictures/Test.png"))

    def possible_movements(self):
        pass

    def cross(self):
        cross_possible_movements = list()
        (W, E, N, S) = (True, True, True, True)
        for changer in range(1, self.range + 1):
            if W:
                W = True if board_column.find(self.location[0]) + changer < 8 else False
            if E:
                E = True if board_column.find(self.location[0]) - changer > 0 else False
            if N:
                N = True if int(self.location[1]) + changer <= 8 else False
            if S:
                S = True if int(self.location[1]) - changer > 0 else False

            if W:
                column = board_column[board_column.find(self.location[0]) + changer]
                row = self.location[1]
                if main_board.board_data[f"{column}{row}"][1] is None:
                    cross_possible_movements.append(f"{column}{row}")
                elif main_board.board_data[f"{column}{row}"][1].white is not self.white:
                    cross_possible_movements.append(f"{column}{row}")
                    W = False
                elif cross_possible_movements.append(f"{column}{row}").white is self.white:
                    W = False
            if E:
                column = board_column[board_column.find(self.location[0]) - changer]
                row = self.location[1]
                if main_board.board_data[f"{column}{row}"][1] is None:
                    cross_possible_movements.append(f"{column}{row}")
                elif main_board.board_data[f"{column}{row}"][1].white is not self.white:
                    cross_possible_movements.append(f"{column}{row}")
                    E = False
                elif cross_possible_movements.append(f"{column}{row}").white is self.white:
                    E = False

            if N:
                column = self.location[0]
                row = int(self.location[1]) + changer
                if main_board.board_data[f"{column}{row}"][1] is None:
                    cross_possible_movements.append(f"{column}{row}")
                elif main_board.board_data[f"{column}{row}"][1].white is not self.white:
                    cross_possible_movements.append(f"{column}{row}")
                    N = False
                elif cross_possible_movements.append(f"{column}{row}").white is self.white:
                    N = False

            if S:
                column = self.location[0]
                row = int(self.location[1]) - changer
                if main_board.board_data[f"{column}{row}"][1] is None:
                    cross_possible_movements.append(f"{column}{row}")
                elif main_board.board_data[f"{column}{row}"][1].white is not self.white:
                    cross_possible_movements.append(f"{column}{row}")
                    S = False
                elif cross_possible_movements.append(f"{column}{row}").white is self.white:
                    S = False

        return cross_possible_movements

    def diagonal(self):
        ####################################################
        # p=positive n= negative
        ####################################################
        (pp, pn, np, nn) = (True, True, True, True)
        possible_diagonal_movements = list()
        #############################
        #   board border check
        #############################
        for row in range(1, self.range + 1):
            if pp:
                pp = True if board_column.index(self.location[0]) + row < 8 and (
                        (int(self.location[1]) - 1) + row) <= 8 else False
            if pn:
                pn = True if board_column.index(self.location[0]) + row < 8 and (
                        (int(self.location[1]) - 1) - row) >= 0 else False
            if nn:
                nn = True if board_column.index(self.location[0]) - row >= 0 and (
                        (int(self.location[1]) - 1) - row) >= 0 else False
            if np:
                np = True if board_column.index(self.location[0]) - row >= 0 and (
                        (int(self.location[1]) - 1) + row) <= 8 else False
            if pp:
                column = board_column[board_column.index(self.location[0]) + row]
                roww = int(self.location[1]) + row
                if main_board.board_data[f"{column}{roww}"][1] is None:
                    possible_diagonal_movements.append(f"{column}{roww}")
                elif main_board.board_data[f"{column}{roww}"][1].white is not self.white:
                    possible_diagonal_movements.append(f"{column}{roww}")
                    pp = False
                elif main_board.board_data[f"{column}{roww}"][1].white == self.white:
                    pp = False

            if pn:
                column = board_column[board_column.index(self.location[0]) + row]
                roww = int(self.location[1]) - row
                if main_board.board_data[f"{column}{roww}"][1] is None:
                    possible_diagonal_movements.append(f"{column}{roww}")
                elif main_board.board_data[f"{column}{roww}"][1].white is not self.white:
                    possible_diagonal_movements.append(f"{column}{roww}")
                    pn = False
                elif main_board.board_data[f"{column}{roww}"][1].white == self.white:
                    pn = False

            if nn:
                column = board_column[board_column.index(self.location[0]) - row]
                roww = int(self.location[1]) - row
                if main_board.board_data[f"{column}{roww}"][1] is None:
                    possible_diagonal_movements.append(f"{column}{roww}")
                elif main_board.board_data[f"{column}{roww}"][1].white is not self.white:
                    possible_diagonal_movements.append(f"{column}{roww}")
                    nn = False
                elif main_board.board_data[f"{column}{roww}"][1].white == self.white:
                    nn = False
            if np:
                column = board_column[board_column.index(self.location[0]) - row]
                roww = int(self.location[1]) + row
                if main_board.board_data[f"{column}{roww}"][1] is None:
                    possible_diagonal_movements.append(f"{column}{roww}")
                elif main_board.board_data[f"{column}{roww}"][1].white is not self.white:
                    possible_diagonal_movements.append(f"{column}{roww}")
                    np = False
                elif main_board.board_data[f"{column}{roww}"][1].white == self.white:
                    np = False
        return possible_diagonal_movements


class Queen(Piece):
    def __init__(self, white, location, range=9):
        super().__init__(white, location, range)
        if self.white:
            self.image = ImageTk.PhotoImage(Image.open("pictures/pices/white_queen.png"))
        else:
            self.image = ImageTk.PhotoImage(Image.open("pictures/pices/white_queen.png"))

    def possible_movements(self):
        self.possible_movements_list += self.diagonal()
        self.possible_movements_list += self.cross()


class King(Piece):
    def __init__(self, white, location, range=1):
        super().__init__(white, location, range)
        if self.white:
            self.image = ImageTk.PhotoImage(Image.open("pictures/pices/white_king.png"))
        else:
            self.image = ImageTk.PhotoImage(Image.open("pictures/pices/white_king.png"))

    def possible_movements(self):
        self.possible_movements_list += self.diagonal()
        self.possible_movements_list += self.cross()


main_board = Board()
white_queen = Queen(True, "a3")
white_queen1 = Queen(True, "c5")
main_board.board_data["c5"][1] = white_queen1
# white_queen.range = 10
print(white_queen.possible_movements())
# print(white_queen.possible_movements())
root.mainloop()
