import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def draw_rainbow(centerX, centerY, start_radius, rb_line_width):
    for i in range(7):
        sd.circle(sd.Point(centerX, -centerY+i*20, ), radius=start_radius, color=rainbow_colors[i], width=rb_line_width)

def draw_wall(wall_width, wall_height, brick_width, brick_height, wall_start_x, wall_start_y, color):

    border_line__left_start = sd.get_point(wall_start_x, wall_start_y)
    border_line_left_end = sd.get_point(wall_start_x, wall_start_y + wall_height)
    sd.line(border_line__left_start, border_line_left_end, color)  # Левая граница

    border_line_right_end = sd.get_point(wall_start_x + wall_width, wall_start_y + wall_height)
    border_line_right_start = sd.get_point(wall_start_x + wall_width, wall_start_y)
    sd.line(border_line_left_end, border_line_right_end, color)    # Верхняя граница
    sd.line(border_line_right_start, border_line_right_end, color)     # Правая граница

    for horizontal_line in range(wall_start_y, wall_height + wall_start_y, brick_height):
        start_line_point = sd.get_point(wall_start_x, horizontal_line)
        end_line_point = sd.get_point(wall_width + wall_start_x, horizontal_line)
        sd.line(start_line_point, end_line_point, color)

        if (horizontal_line + brick_height) % (brick_height * 2):
            x_shift = brick_width / 2
        else:
            x_shift = 0

        for vertical_line in range(wall_start_x, wall_width + wall_start_x, brick_width):
            start_line_point = sd.get_point(vertical_line + x_shift, horizontal_line)
            end_line_point = sd.get_point(vertical_line + x_shift, horizontal_line + brick_height)
            sd.line(start_line_point, end_line_point, color)
    v1 = sd.get_vector(start_point=sd.get_point(100, 480), angle=30, length=347, width=3)
    v2 = sd.get_vector(start_point=sd.get_point(700, 480), angle=150, length=347, width=3)
    v1.draw(color=color)
    v2.draw(color=color)