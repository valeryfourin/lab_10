'''
Реалізувати програмно мовою Python завдання з наведеного нижче списку. Для
кожної з задач алгоритм реалізувати з використанням рекурсії і ітерації. Аргументувати
письмово доцільність вибору в кожному випадку рекурсії або ітерації (використовувати
в якості критеріїв - час розробки та виконання програм, обсяг займаної пам'яті,
читабельність програми).

Наталію Артурівну з днем народження! :)

Виконала Новіцька В.І. 122Б
'''
import random
import numpy as np
import time
from datetime import datetime
while True:
    while True:
        try:
            answer_task = int(input("\nPlease type '1' if you want to return a string backwards,"
                                "\ntype '2' if you want to determine whether your number is prime,"
                                "\ntype '3' if you want to convert decimal number into hexadecimal: "))
            # вибір на виконання однієї з трьох програм з додаткових індивідуальних завдань

        except TypeError and ValueError:  #  перевірка на помилки
            print('Error. Please input only integers.\n')
            continue

        if answer_task == 1:
            # Сформувати функцію для введення з клавіатури послідовності чисел і виведення
            # її на екран у зворотному порядку (завершаючий символ послідовності – крапка)
            while True:
                seq = input("Please input sequence of numbers (must end with '.'): ")
                if seq[-1] != '.':
                    print("\nError! Must end with '.'")  # послідовність повинна закінчуватись крапкою
                    continue
                else:
                    break

            def backwards_recur(seq, seq_b=[], i=-1):  # запис послідовності у зворотньому порядку рекурсивно
                seq_b.append(seq[i])
                i -= 1  # у послідовність додаються елементи, початок з кінця, крок -1

                if (seq_b[0] == '.') and (len(seq_b) == len(seq)):
                    # якщо на першому місці крапка, і у масив були додані всі елементи у звор. порядку з
                    # вихідного масиву, то видалимо крапку на першому місці і додамо в кінці (так потрібно за умовою)
                    # друга умова необхідна для того, щоб програма не завершила виконання, коли а перму місці крапка
                    # (з крапки починається зберігання елементів у масив, бо вона на останньому місці)
                    del seq_b[0]
                    seq_b = ''.join(seq_b) + '.'
                    return seq_b
                return backwards_recur(seq, seq_b, i)

            def backwards_iter(seq, seq_b = []):  # запис послідовності у зворотньому порядку ітераційно
                for i in range(-1, -(len(seq)+1), -1):
                    seq_b.append(seq[i])
                del seq_b[0]
                seq_b = ''.join(seq_b) + '.'
                return seq_b
            # робота аналогічна до рекурсивної функції, заміть лічильників використовуємо цикли

            start11 = datetime.now()
            time.sleep(1)
            num_back_recur = backwards_recur(seq)
            end11 = datetime.now()
            start12 = datetime.now()
            time.sleep(1)
            num_back_iter = backwards_iter(seq)
            end12 = datetime.now()

            print(f'Your sequence \n{seq} \nturned backwards using recursion: \n{num_back_recur}'
                  f' \nexcecution time: {end11-start11}\nturned backwards using iteration: \n{num_back_iter} '
                  f'\nexcecution time: {end12-start12}')

        elif answer_task == 2:
            # Сформувати функцію, що визначатиме чи є задане натуральне число простим.
            # Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
            # себе).
            while True:
                try:
                    n = int(input('\nInput a number: '))
                    if n < 0:
                        raise ValueError('\nError! Number must be positive.')  # перевірка на додатнє число
                    else:
                        break
                except TypeError and ValueError:  # перевірка на помилки
                    print('\nError. Please input only integers.\n')
                    continue

            def prime_num_recur(n, counter=0, i=1):  # функція, що визначає, чи є число простим, рекурсивно
                if i == (n + 1):  # n+1, оскільки потрібно, щоб відбулось ділення числа на самого себе
                    if counter == 2:  # якщо к-ть чисел, на які ділиться задане число 2, то воно є простим
                        return True
                    else:  # в інакшому випадкому число не є простим
                        return False
                else:
                    if n % i == 0:
                        counter += 1
                        # будемо ділити задане число по черзі на всі числа, від 1 до самого цього числа
                        # якщо при діленні остача = 0, то записуємо у лічильник +1
                    i += 1  # к-ть ділень
                    return prime_num_recur(n, counter, i)

            def prime_num_iter(n, counter = 0):  # функція, що визначає, чи є число простим, ітераційно
                for i in range(1, n + 1):
                    if n % i == 0:
                        counter += 1  # якщо при діленні остача = 0, то записуємо у лічильник +1
                if counter == 2:  # якщо к-ть чисел, на які ділиться задане число 2, то воно є простим
                    return True
                else:  # в інакшому випадкому число не є простим
                    return False


            start21 = datetime.now()
            time.sleep(1)
            num_prime_recur = prime_num_recur(n)
            end21 = datetime.now()
            start22 = datetime.now()
            time.sleep(1)
            num_prime_iter = prime_num_iter(n)
            end22 = datetime.now()

            print(f'Your number {n} is prime. Result \n using recursion {num_prime_recur} \nexcecution time: '
                  f'{end21-start21}\n using iteration {num_prime_iter} \nexcecution time: {end22-start22}')

        elif answer_task == 3:
            # Сформувати функцію для переведення натурального числа з десяткової системи числення у шістнадцятирічну.
            while True:
                try:
                    n = int(input('\nInput a number: '))
                    if n < 0:
                        raise ValueError('\nError! Number must be positive.')  # перевірка на додатнє число
                    else:
                        break
                except TypeError and ValueError:  # перевірка на помилки
                    print('\nError. Please input only integers.\n')
                    continue

            def hexadecim_recur(n, hex_name=''):
                # переведення натурального числа з десяткової системи числення у шістнадцятирічну рекурсивно
                if n == 0:
                    hex_name += str(n)
                    return hex_name[::-1]  # виведення у зворотньому порядку
                else:
                    mod = n // 16
                    num = n % 16
                    if num < 10:
                        hex_name += str(num)
                    elif num == 10:
                        hex_name += 'A'
                    elif num == 11:
                        hex_name += 'B'
                    elif num == 12:
                        hex_name += 'C'
                    elif num == 13:
                        hex_name += 'D'
                    elif num == 14:
                        hex_name += 'E'
                    elif num == 15:
                        hex_name += 'F'
                    return hexadecim_recur(mod, hex_name)
            # щоб перетворити число, потрібно ділити його націло на 16, доки не отримаємо результатом нуль.
            # Для усіх цих результатів, включаючи вихідне число. потрібно знайти остачу від ділення і записати ці
            # цифри у зворотньому порядку. Для чисел 10-15 відповідними позначеннями будуть A-F

            def hexadecim_iter(num):
                # переведення натурального числа з десяткової системи числення у шістнадцятирічну ітераційно
                hex_name = ''
                while num >= 0:
                    mod = num % 16
                    num = num // 16

                    if mod == 10:
                        hex_name += 'A'
                    elif mod == 11:
                        hex_name += 'B'
                    elif mod == 12:
                        hex_name += 'C'
                    elif mod == 13:
                        hex_name += 'D'
                    elif mod == 14:
                        hex_name += 'E'
                    elif mod == 15:
                        hex_name += 'F'
                    else:
                        hex_name += str(mod)

                    if num == 0:
                        mod = num % 16
                        num = num // 16
                        hex_name += str(mod)
                        break
                return hex_name[::-1]  # виведення у зворотньому порядку


            start31 = datetime.now()
            time.sleep(1)
            num_hex_recur = hexadecim_recur(n)
            end31 = datetime.now()
            start32 = datetime.now()
            time.sleep(1)
            num_hex_iter = hexadecim_iter(n)
            end32 = datetime.now()

            print(f'Your number {n} in hexadecimal notation.\n using recursion {num_hex_recur} \n excecution time:'
                  f' {end31-start31} \n using iteration {num_hex_iter} \n excecution time: {end32-start32}')

        else:
            print("\nError! Input '1', '2' or '3'.")
            continue
        break

    answer = input('\nDo you want to continue? Yes-1, No-2:')
    if answer == '1':
        continue
    else:
        break