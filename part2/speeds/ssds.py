def get_ssd_params(calc_capasity):
    speed = 500

    return round(calc_capasity*1024/(speed*8), 2)
