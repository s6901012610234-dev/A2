from processing import *

grid_size = [10,10]
screen_size = [500,500]
grid = []

#===============================setup========================================

def setup():
    size(screen_size[0],screen_size[1])
    strokeWeight(3)
    y = 0
    while y < grid_size[1]:
        row = []
        x = 0
        while x < grid_size[0]:
            row.append(0)
            x = x + 1
        grid.append(row)
        y = y + 1


#def fillin():


#def visual():


#def three_del():


#def fall():


#def mousePressed():


def draw():
    background(255)
    cell_width = screen_size[0] / grid_size[0]
    cell_height = screen_size[1] / grid_size[1]
    i = 0
    while i <= grid_size[0]:
        x = i * cell_width
        line(x, 0, x, screen_size[1])
        i = i + 1

    i = 0
    while i <= grid_size[1]:
        y = i * cell_height
        line(0, y, screen_size[0], y)
        i = i + 1

    y = 0
    while y < grid_size[1]:
        x = 0
        while x < grid_size[0]:
            cx = (x * cell_width) + (cell_width / 2)
            cy = (y * cell_height) + (cell_height / 2)
            fill(200)
            ellipse(cx, cy, cell_width * 0.6, cell_height * 0.6)
            x = x + 1
        y = y + 1


run()