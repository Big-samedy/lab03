import simple_draw as sd

def rand_delta(number, percent=50, is_positive=False):
    if is_positive:
        rand = sd.random_number(0, percent * 10) / 1000
    else:
        rand = sd.random_number(-percent * 10, percent * 10) / 1000

    return number * rand


def branch_width_color(length):
    if length > 50:
        width = 4
        color = (139, 69, 19)
    elif length > 30:
        width = 3
        color = (128, 128, 0)
    elif length > 15:
        width = 2
        color = (107, 142, 35)
    elif length < 15:
        width = 1
        color = (124, 252, 0)

    return width, color


def draw_branches(start_point, start_angle, branch_length, width=1, color=(139, 69, 19)):

    if branch_length < 5:
        return

    width, color = branch_width_color(branch_length)

    start_point = sd.vector(start_point, start_angle, branch_length, color, width)
    delta = int(20 + rand_delta(30, percent=20))
    branch_length *= (.6 + rand_delta(0.6, percent=20, is_positive=True))
    shift_angle = start_angle + delta
    draw_branches(start_point, shift_angle, branch_length, width, color)

    shift_angle = start_angle - delta
    draw_branches(start_point, shift_angle, branch_length, width, color)

def draw_smile(x, y, color):
    x -= 60
    y -= 50
    start_point = sd.Point(x, y)
    sd.circle(start_point, 50, color, 3)
    sd.line(sd.Point(x-25, y-10), sd.Point(x-10, y-20), color, 3)
    sd.line(sd.Point(x-10, y-20), sd.Point(x+10, y-20), color, 3)
    sd.line(sd.Point(x+10, y-20), sd.Point(x+25, y-10), color, 3)
    sd.circle(sd.Point(x-17.5, y+12.5), 10, color, 3)
    sd.circle(sd.Point(x+17.5, y+12.5), 10, color, 3)

def draw_window(left_bottom, right_top, color):
    sd.rectangle(left_bottom, right_top, color)
