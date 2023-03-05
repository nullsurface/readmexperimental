from .Color import Color

class Cell:
    color: Color
    x_pos: int
    y_pos: int

    def __init__(self, x_pos: int, y_pos: int, color: Color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color

    def set_pos(self, x_pos: int, y_pos: int):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def set_color(self, color: Color):
        self.color = color
