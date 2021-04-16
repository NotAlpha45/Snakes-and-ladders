from tkinter import *
from PIL import Image, ImageTk
import random


def in_position(x, y, x1, y1, x2, y2):
    """
    Parameters: x, y, x1, y1, x2, y2 (coordiantes of a point and two other check points)\n
    Action: Chcks if (x,y) is beteen (x1, y1) and (x2, y2)
    """
    if x1 <= x <= x2 and y1 <= y <= y2:
        return True
    else:
        return False


def block_number(x, y):
    """
    Parameters : x, y ( x and y coordinate of a point)\n
    Action : Returns the block number in which the point is.
    """
    # block_coor is a list of all the blocks of the game board with their
    # (x1, y1) and (x2, y2) coordinates and their sequence number. Tuple
    # format (x1, y1, x2, y2, number)
    block_coor = [
        (0, 0, 80, 80, 21),  # 1
        (84, 0, 164, 80, 22),  # 2
        (168, 0, 244, 80, 23),  # 3
        (248, 0, 328, 80, 24),  # 4
        (332, 0, 412, 80, 25),  # 5
        (0, 84, 80, 164, 20),  # 6
        (84, 84, 164, 164, 19),  # 7
        (168, 84, 244, 164, 18),  # 8
        (248, 84, 328, 164, 17),  # 9
        (332, 84, 412, 164, 16),  # 10
        (0, 168, 80, 244, 11),  # 11
        (84, 168, 164, 244, 12),  # 12
        (168, 168, 244, 244, 13),  # 13
        (248, 168, 328, 244, 14),  # 14
        (332, 168, 412, 244, 15),  # 15
        (0, 248, 80, 328, 10),  # 16
        (84, 248, 164, 328, 9),  # 17
        (168, 248, 244, 328, 8),  # 18
        (248, 248, 328, 328, 7),  # 19
        (332, 248, 412, 328, 6),  # 20
        (0, 332, 80, 412, 1),  # 21
        (84, 332, 164, 412, 2),  # 22
        (168, 332, 244, 412, 3),  # 23
        (248, 332, 328, 412, 4),  # 24
        (332, 332, 412, 412, 5),  # 25
    ]
    for section in block_coor:
        x1 = section[0]
        y1 = section[1]
        x2 = section[2]
        y2 = section[3]
        number = section[4]
        if in_position(x, y, x1, y1, x2, y2):
            return number


def row_val(x, y):
    """
    Parameters: x,y (x and y coordinates of a point) \n
    Action: Returns the number of the board row in which the point is.
    """
    if 1 <= block_number(x, y) <= 5:
        return 1
    if 6 <= block_number(x, y) <= 10:
        return 2
    if 11 <= block_number(x, y) <= 15:
        return 3
    if 16 <= block_number(x, y) <= 20:
        return 4
    if 21 <= block_number(x, y) <= 25:
        return 5


class Player:
    def __init__(self, canvas, name, image):
        self.name = name
        self.image = image
        self.canvas = canvas
        self.__x = None
        self.__y = None
        self.has_won = False
        self.__move_counter = 0
        self.__remaining_move = 0
        self.__row_val = None

    def set_pos(self, x, y):
        """
        Parameters: x, y (x and y coordinates of the point to be moved to)\n
        Action: Sets  player's x and y position and the row in which they are moved.
        """
        self.__x = x
        self.__y = y
        self.__row_val = row_val(x, y)

    def get_pos(self):
        return self.__x, self.__y

    def show_win(self, win_img):
        """
        Parameters: win_img (image needed to display. Should be a PhotoImage object)\n
        Action: Displays the image on screen.
        """
        self.canvas.create_image(self.__x, self.__y, image=self.image)

    def draw(self):
        """
        Parameters: None\n
        Action: Draws the player image in it's current position.
        """
        # self.canvas.image = self.image
        self.canvas.create_image(self.__x, self.__y, image=self.image)
        # self.canvas.move(self.image, self.__x, self.__y)

    def move(self, dice_val):
        """
        Parameters: dice value\n
        Action: Moves the player according to the dice number and board configuration.
        """
        self.__remaining_move = dice_val
        skip_a_move = False

        # Regular sequential move of the player.
        while self.__remaining_move > 0:

            if self.__row_val == 1 and block_number(self.__x, self.__y) == 5:
                self.set_pos(332 + 40, 248 + 40)
                skip_a_move = True
                if self.__remaining_move == 1:
                    self.draw()
                    break

            if self.__row_val == 2 and block_number(self.__x, self.__y) == 10:
                self.set_pos(0 + 40, 168 + 40)
                skip_a_move = True
                if self.__remaining_move == 1:
                    self.draw()
                    break

            if self.__row_val == 3 and block_number(self.__x, self.__y) == 15:
                self.set_pos(332 + 40, 84 + 40)
                skip_a_move = True
                if self.__remaining_move == 1:
                    self.draw()
                    break

            if self.__row_val == 4 and block_number(self.__x, self.__y) == 20:
                self.set_pos(0 + 40, 0 + 40)
                skip_a_move = True
                if self.__remaining_move == 1:
                    self.draw()
                    break

            if self.__row_val == 5 and block_number(self.__x, self.__y) == 25:
                self.has_won = True

            # If the row number is 1, 3 or 5 and there isn't a skipping move and the player
            # will be in the board after the move, then the player moves in foreward direction.
            if (
                (self.__row_val == 1 or self.__row_val == 3 or self.__row_val == 5)
                and skip_a_move == False
                and in_position(self.__x + 82, self.__y, 0, 0, 412, 412) == True
            ):
                self.__x += 82

            if (
                (self.__row_val == 2 or self.__row_val == 4)
                and (skip_a_move == False)
                and in_position(self.__x - 82, self.__y, 0, 0, 412, 412) == True
            ):
                self.__x -= 82

            skip_a_move = False
            self.__remaining_move -= 1

        # Climbing ladder at number 5
        if self.__row_val == 1 and block_number(self.__x, self.__y) == 5:
            self.set_pos(332 + 40, 84 + 40)

        # Climbing ladder at number 9
        if self.__row_val == 2 and block_number(self.__x, self.__y) == 9:
            self.set_pos(84 + 40, 84 + 40)

        # Climbing ladder at number 12
        if self.__row_val == 3 and block_number(self.__x, self.__y) == 13:
            self.set_pos(168 + 40, 0 + 40)

        # Bit by snake at number 8
        if self.__row_val == 2 and block_number(self.__x, self.__y) == 8:
            self.set_pos(168 + 40, 332 + 40)

        # Bit by snake at number 20
        if self.__row_val == 4 and block_number(self.__x, self.__y) == 20:
            self.set_pos(0 + 40, 0 + 40)

        # Bit by snake at number 24
        if self.__row_val == 5 and block_number(self.__x, self.__y) == 24:
            self.set_pos(248 + 40, 84 + 40)

        self.draw()
