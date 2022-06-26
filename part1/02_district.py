#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from district.soviet_street.house1 import room1
from district.soviet_street.house1 import room2
from district.soviet_street.house2 import room1
from district.soviet_street.house2 import room2
from district.central_street.house1 import room1
from district.central_street.house1 import room2
from district.central_street.house2 import room1
from district.central_street.house2 import room2

mods = sys.modules.keys()


def get_rooms(mods):
    rooms_agrs = []
    for mod in mods:
        if mod[0:8] == 'district' and mod[-2:] in ['m1', 'm2']:
            rooms_agrs.append(sys.modules.get(mod).folks)
    return rooms_agrs


roommates = [", ".join(mate) for mate in get_rooms(mods)]

print(f'На районе живут: {", ".join(roommates)}')

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
