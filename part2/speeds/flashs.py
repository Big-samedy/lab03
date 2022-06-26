def get_flash_params(calc_capasity):
    speed = 300

    return round(calc_capasity*1024/(speed*8), 2)
