def step2_umbrella():
    print(
        'Утка-маляр пошла с зонтиком в бар.'
        'Когда пошёл дождь, у утки было меланхоличное настроение,'
        'поэтому она не стала использовать зонтик,'
    )
    return step3_exit(True)


def step2_no_umbrella():
    print(
        'Утка-маляр пошла в бар без зонтика. '
        'Когда пошёл дождь, она не расстроилась,'
        'ведь утки не боятся воды и не промокают. '

    )
    return step3_exit(False)


def step3_exit(ending):
    if ending:
        print(
            'Дождь и вкусный коктейль помогли утке забыть '
            'про свою сложную работу, поэтому она'
            'возвращалась домой счастливой. '
        )
    else:
        print(
            'Ситуация и коктейли наталкнули утку на мысль, '
            'что зонтик ей вообще не нужен, '
            'поэтому когда она пришла домой, '
            'то решила подарить свой зонт.'
        )

def step1():
    print(
        'Утка-маляр решила выпить зайти в бар. '
        'Взять ей зонтик?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
