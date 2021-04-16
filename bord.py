from tkinter import *
from PIL import Image, ImageTk
import random
import turtle
import player


def dice():
    return random.randint(1, 6)


def roll_dice(canvas):
    dice_face = {
        1: "dice1.gif",
        2: "dice2.gif",
        3: "dice3.gif",
        4: "dice4.gif",
        5: "dice5.gif",
        6: "dice6.gif",
    }
    roll_dice_val = dice()
    dice_img = PhotoImage(file=r"Assets/" + dice_face[roll_dice_val])
    canvas.dice_img = dice_img  # To prevent asset from being garbage collected.
    canvas.create_image(225, 450, image=dice_img)
    return roll_dice_val


def place_ladder(canvas):
    """
    Parameters : canvas (the canvas to be drawn on)\n
    Action : Loads all the ladder images and places them on the canvas.
    """
    ladder = PhotoImage(file=r"Assets/ladder.gif")
    canvas.ladder = ladder
    canvas.create_image(168 + 40, 84 + 40, image=ladder)

    ladder1 = PhotoImage(file=r"Assets/ladder2.gif")
    canvas.ladder1 = ladder1
    canvas.create_image(84 + 40, 248 - 40, image=ladder1)

    ladder2 = PhotoImage(file=r"Assets/ladder3.gif")
    canvas.ladder2 = ladder2
    canvas.create_image(332 + 40, 248, image=ladder2)


def place_snake(canvas):
    """
    Parameters : canvas (the canvas to be drawn on)\n
    Action : Loads all the snake images and places them on the canvas.
    """
    snake = PhotoImage(file=r"Assets/snake.gif")
    canvas.snake = snake
    canvas.create_image(168 + 40, 248 + 80, image=snake)

    snake1 = PhotoImage(file=r"Assets/snake2.gif")
    canvas.snake1 = snake1
    canvas.create_image(248 + 40, 84, image=snake1)

    snake2 = PhotoImage(file=r"Assets/snake3.gif")
    canvas.snake2 = snake2
    canvas.create_image(0 + 40, 248, image=snake2)


def make_grid(canvas, color):
    # Holds the positions for all the blocks in the game (starting from top left)
    # format = (x1, y1, x2, y2, block_num)
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
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        canvas.create_text(x1 + 10, y1 + 10, text=f"{number}")


def game_turn(canvas, p):
    p.move(roll_dice(canvas))


def make_board():
    window = Tk()
    window.title("Snake and Ladder")
    window.geometry("700x500")
    canvas = Canvas(window, width=450, height=700, bg="white")
    canvas.grid(padx=0, pady=0)
    make_grid(canvas, "white")
    place_snake(canvas)
    place_ladder(canvas)
    bull_img = PhotoImage(file=r"Assets/bull.gif")
    bull = player.Player(canvas, "Mr. bull", bull_img)
    bull.set_pos(0 + 40, 332 + 40)
    bull.draw()
    dice_button = Button(
        window, text="Roll Dice!", command=lambda: game_turn(canvas, bull)
    )
    dice_button.grid(column=2, row=0)

    window.mainloop()


make_board()
