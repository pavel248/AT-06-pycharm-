from PIL import Image
import numpy as np


def paint_area_in_gray(area, gray_scale, step):
    area_height = len(area)
    area_width = len(area[0])
    for area_cur_row in range(area_height):
        for area_cur_column in range(area_width):
            area[area_cur_row][area_cur_column][0] = gray_scale // step * step
            area[area_cur_row][area_cur_column][1] = gray_scale // step * step
            area[area_cur_row][area_cur_column][2] = gray_scale // step * step


def get_gray_scale_for_area(area):
    area_height = len(area)
    area_width = len(area[0])
    area_scale = 0
    for area_cur_row in range(area_height):
        for area_cur_col in range(area_width):
            r, g, b = area[area_cur_row, area_cur_col][0], area[area_cur_row, area_cur_col][1], area[area_cur_row, area_cur_col][2]
            area_scale += (int(r) + int(g) + int(b))//3
    return area_scale // (area_height ** 2)


def get_gray_image(img_arr, size, step):
    current_row = 0
    height = len(arr)
    width = len(arr[1])
    while current_row < height:
        current_column = 0
        while current_column < width:
            area = img_arr[current_row:current_row + size, current_column:current_column + size]
            gray_scale = get_gray_scale_for_area(area)
            paint_area_in_gray(area, gray_scale, step)
            current_column += size
        current_row += size
    return Image.fromarray(img_arr)

img = Image.open("img2.jpg")
arr = np.array(img)
size = int(input('Длина одной плитки мозаики: '))
step = int(255 / int(input('Кол-во шагов градации серого цвета: ')))

res = get_gray_image(arr, size, step)
res.save('res.jpg')
