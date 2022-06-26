def get_hdd_params(calc_capasity):
    speed = 150

    return round(calc_capasity*1024/(speed*8), 2)
