from processing import *
import random

grid_size = [10,10]
screen_size = [500,500]
grid = []
colour = [[255,100,100],[100,255,100],[100,100,255]]

#-------------------------------=-setup---------------------------------------

def setup():
    size(screen_size[0],screen_size[1])
    strokeWeight(3)
    x = 0
    while x < grid_size[1]:
        row = []
        y = 0
        while y < grid_size[0]:
            row.append(0)
            y = y + 1
        grid.append(row)
        x = x + 1


def fillin():
    a = 0
    while a < grid_size[1]:
        b = 0
        while b < grid_size[0]:
            if grid[a][b] == 0:
                grid[a][b] = random.randint(1,3)
            b = b + 1
        a = a + 1


#def visual():


#def three_del():


#def fall():


#def mousePressed():

#----------------------------------draw---------------------------------------

def draw():
    background(255)
    fillin()
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
            colour_index = grid[y][x]
            fill_colour = colour[colour_index - 1]
            fill(fill_colour[0], fill_colour[1], fill_colour[2])
            ellipse(cx, cy, cell_width * 0.6, cell_height * 0.6)
            x = x + 1
        y = y + 1


run()