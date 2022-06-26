ingredients = {
    'bun': False,
    'cutlet': False,
    'cucumber': False,
    'tomato': False,
    'mayonnaise': False,
    'cheese': False,
    'sauce': False
}


def add_bun(current_ingredients):
    current_ingredients['bun'] = True
    print('На самом вверху булочка')
    return True


def add_cutlet(current_ingredients):
    if current_ingredients['bun']:
        current_ingredients['cutlet'] = True
        print('Теперь положим котлету')
        return True
    else:
        print('Неправильный порядок ингридиетов. Начните с булочки')
        return False


def add_cucumber(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['cucumber'] = True
        print('А сейчас добавим огурчик')
        return True
    else:
        print('Неправильный порядок ингридиетов. Начните с булочки и котлеты')
        return False


def add_tomato(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['tomato'] = True
        print('А теперь добавляем помидор')
        return True
    else:
        print('Неправильный порядок ингридиетов. Начните с булочки и котлеты')
        return False


def add_cheese(current_ingredients):
    if current_ingredients['bun']:
        current_ingredients['cheese'] = True
        print('Добавляем сыр')
        return True
    else:
        print('Неправильный порядок ингридиетов. Начните с булочки')
        return False


def add_mayonnaise(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['mayonnaise'] = True
        print('Заправляем майонезом')
        return True
    else:
        print('Неправильный порядок ингридиетов. Начните с булочки и котлеты')
        return False


def add_sauce(current_ingredients):
    if current_ingredients['bun'] and current_ingredients['cutlet']:
        current_ingredients['sauce'] = True
        print('Заправляем соусом')
        return True
    else:
        print('Неправильный порядок ингридиетов. Начните с булочки и котлеты')
        return False
