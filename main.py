import cmath
import os


def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def solve(*coefficients):
    if 0 < len(coefficients) <= 3:
        coeff = list(coefficients[::])
        for i in range(2):
            if len(coeff) == 3:
                break
            coeff.insert(0, 0)
        a, b, c = float(coeff[0]), float(coeff[1]), float(coeff[2])
        roots = set()
        if a == 0 and b == 0:
            print('все числа' if c == 0 else 'ложь')
        elif a != 0:
            if b != 0:
                d = (b ** 2) - 4 * a * c
                if d < 0:
                    roots.add(str((- b + cmath.sqrt(d)) / (2 * a)).replace('(', '').replace(')', ''))
                    roots.add(str((- b - cmath.sqrt(d)) / (2 * a)).replace('(', '').replace(')', ''))
                else:
                    roots.add((- b + d ** 0.5) / (2 * a))
                    roots.add((- b - d ** 0.5) / (2 * a))
            else:
                print(((-c / a) ** 0.5, -(-c / a) ** 0.5) if c * a < 0 else 'ложь')
        else:
            roots.add(- c / b)
        while len(roots) != 0:
            print(f'x = {roots.pop()}')
    else:
        print('Mistakes were made!')


def main():
    while True:
        print('Выберите действие которое хотите сделать:\n'
              'Сложить: +\n'
              'Вычесть: -\n'
              'Умножить: \n'
              'Поделить: /\n'
              'div: //\n'
              'mod: %\n'
              'корень любой степени из числа : root\n'
              'возведение в степень: **\n'
              'Посчитать выражение: =\n'
              'Найти корни квадратного уравнения: 2\n'
              'Выйти: q\n')
        action = input('Действие: ')
        if action == 'q':
            print('The end.')
            break
        if action in ('+', '-', '*', '/', '//', '%', '**', 'root'):
            try:
                x = float(input('x = '))
                y = float(input('y = '))
            except:
                print('Mistakes were made!')
                continue
            if action == '+':
                print(f'{x} + {y} = {x + y}')
            elif action == '-':
                print(f'{x} - {y} = {x - y}')
            elif action == '*':
                print(f'{x} * {y} = {x * y}')
            elif action == '/':
                if y != 0:
                    print(f'{x} / {y} = {x / y}')
                else:
                    print('Mistakes were made!')
            elif action == '//':
                if y != 0:
                    print(f'{x} // {y} = {x // y}')
                else:
                    print('Mistakes were made!')
            elif action == '%':
                if y != 0:
                    print(f'{x} % {y} = {x % y}')
                else:
                    print('Mistakes were made!')
            elif action == '**':
                if (x != 0) and (y >= 0):
                    print(f'{x} ** {y} = {x ** y}')
                else:
                    print('Mistakes were made!')
            elif action == 'root':
                try:
                    print(f'root {y} degree of {x} = {x ** float(1 / y)}')
                except:
                    print('Mistakes were made!')
        elif action == '=':
            inp = input('Enter expression:')
            try:
                print(f'inp = {eval(inp)}')
            except:
                print('Mistakes were made!')
        elif action == '2':
            solve(*input('Enter coefficients split with space: ').split(' '))
        else:
            print('Mistakes were made!')
        input('press Enter to continue...')
        clearconsole()  # работает именно в cmd или в терминале


main()
