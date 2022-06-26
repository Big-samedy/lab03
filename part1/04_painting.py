#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать (или при необходимости написать) функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from my_draw import draw as dl

screen_width = 1400
screen_height = 1000
sd.resolution = (screen_width, screen_height)

rb_centerX = screen_width/2
rb_centerY = screen_height/2-300
rb_start_radius = 1100
rb_line_width = 18

dl.draw_rainbow(rb_centerX, rb_centerY, rb_start_radius, rb_line_width)

brick_width, brick_height = 40, 20
wall_width, wall_height = 600, 400
start_wall_x, start_wall_y = 100, 80
wall_color = (255, 140, 0)

dl.draw_wall(wall_width, wall_height, brick_width, brick_height, start_wall_x, start_wall_y, wall_color)

win_height = 160
win_width = 122
win_color = sd.COLOR_WHITE
win_left_bottom = sd.get_point(wall_width/2 - win_width/2 + start_wall_x, wall_height/2 - win_height/4 + start_wall_y)
win_right_top = sd.get_point(wall_width/2 + win_width/2 + start_wall_x, wall_height/2 + win_height*3/4 + start_wall_y)

dl.draw_window(win_left_bottom, win_right_top, win_color)

dl.draw_smile(int(wall_width/2 + start_wall_x * 2)-40, int(wall_height/2 - start_wall_y) + 250, sd.COLOR_DARK_GREEN)

root_point = sd.get_point(1000, 90)
dl.draw_branches(root_point, 90, 200)

sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
