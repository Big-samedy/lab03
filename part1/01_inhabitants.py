#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import room_1
import room_2


def show_rooms(*args):
    rooms = args
    for room in rooms:
        print(f'В комнате {room.__name__} живут: {", ".join(room.folks)}')
    pass


# show_rooms(room_1, room_2)

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
