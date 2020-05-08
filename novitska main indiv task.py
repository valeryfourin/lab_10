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
            answer_task = int(input("\nPlease type '1' if you want to find a factorial,"
                                "\ntype '2' if you want to find a digital root of a natural number,"
                                "\ntype '3' if you want to find index of a max element: "))
            # вибір на виконання однієї з трьох програм з основних індивідуальних завдань

        except TypeError and ValueError:  #  перевірка на помилки
            print('\nError. Please input only integers.\n')
            continue

        if answer_task == 1:
            # Сформувати функцію, що буде обчислювати факторіал заданого користувачем
            # натурального числа n.

            while True:
                try:
                    number = int(input('\nInput a number to find a factorial for: '))
                    if number < 0:
                        raise ValueError('\nError.Factorial not defined for negative values.') # перевірка на додатнє число
                    else:
                        break
                except TypeError and ValueError:  # перевірка на помилки
                    print('\nError. Please input only integers.\n')
                    continue

            def factorial_recur(number):  # обчислення факторіалу рекурсією
                if number == 0:  # факторіал від нуля одиниця
                    return 1
                else:
                    return number * factorial_recur(number - 1)
                    # факторіал від числа дорівнює добутку усіх чисел від 1 до цього числа

            def factorial_iter(number):  # обчислення факторіалу ітерацією
                num_fact_iter = 1
                if number == 0:
                    num_fact_iter = 1  # факторіал від нуля одиниця
                else:
                    for i in range(1, number+1):
                        num_fact_iter *= i  # добуток усіх чисел від 1 до заданого числа
                return num_fact_iter


            start11 = datetime.now()
            time.sleep(1)
            num_fact_recur = factorial_recur(number)
            end11 = datetime.now()
            start12 = datetime.now()
            time.sleep(1)
            num_fact_iter = factorial_iter(number)
            end12 = datetime.now()

            print(f'Factorial of {number}: \nusing recursion {num_fact_recur} \n excecution time: '
                  f'{end11-start11}; \nusing iteration {num_fact_iter} \n excecution time: {end12-start12}.')

        elif answer_task == 2:
            # Сформувати функцію для обчислення цифрового кореню натурального числа.
            # Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
            # числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
            # сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
            # числа.

            while True:
                try:
                    number = int(input('\nInput a number to find a digital root for: '))
                    if number < 0:
                        raise ValueError('\nError.Digital root not defined for negative values.') # перевірка на додатнє число
                    else:
                        break
                except ValueError or TypeError:
                        print('\nError.Digital root only accepts integral values.')  # перевірка на ціле число


            number = str(number)  # перетворимо число у строку, щоб можна було легко знайти суму цифр

            def digroot_recur(number):  # обчислення цифрового кореню рекурсією
                if len(number) == 1:  # якщо у числі всього одна цифра, то це і є його цифровий корінь
                    return number
                else:
                    sum = 0  # сума цифр
                    for i in number:
                        sum += int(i)
                    number = str(sum)
                    return digroot_recur(number)
                # цифри числа сумуються, якщо отримана сума має більше однієї цифри, вони сумуються, і так, доти
                # не отримаємо одну цифру

            def digroot_iter(number):  # обчислення цифрового кореню ітерацією
                if len(number) == 1:  # якщо у числі всього одна цифра, то це і є його цифровий корінь
                    return number
                else:
                    sum = 0  # сума цифр
                    step = 0
                    # крок потрібен для обчислення суми перший раз, оскільки для наступних обчислень суми
                    # повинна виконуватись умова, що цифр у числі більше однієї
                    while True:
                        if step == 0:
                            for i in number:
                                sum += int(i)
                                step += 1
                        elif sum > 9 and step > 0:  # у числі більше однієї цифри обчислюємо суму далі
                            number = str(sum)
                            sum = 0
                            for i in number:
                                sum += int(i)
                        else:  # число складається з однієї цифри, це і є цифровий корінь
                            return sum

            start21 = datetime.now()
            time.sleep(1)
            num_digroot_recur = digroot_recur(number)
            end21 = datetime.now()
            start22 = datetime.now()
            time.sleep(1)
            num_digroot_iter = digroot_iter(number)
            end22 = datetime.now()

            print(f'Digital root of {number}: \nusing recursion {num_digroot_recur} \n excecution time: '
                  f'{end21-start21}; \nusing iteration {num_digroot_iter} \n excecution time: {end22-start22}.')

        elif answer_task == 3:
            # Сформувати функцію для обчислення індексу максимального елемента масиву n*n, де 1<=n<=5.
            while True:
                n = int(input('\nInput a number of rows or columns in array A: '))
                if n < 0:
                    raise ValueError('\nError. Input positive value.')  # перевірка на додатнє число
                if type(n) is not int:
                    raise ValueError('\nError. Input integral value.')  # перевірка на ціле число
                else:
                    break

            a = np.zeros((n, n), dtype=int)  # створюємо матрицю nхn з усіма 0
            for i in range(n):
                for g in range(n):
                    a[i, g] = random.randint(1,100)

            a_list = []  # зробимо з матриці двовимірний список, щоб простіше знайти максимальне число
            for i in list(a):
                a_list.append(list(i))

            def maxindex_recur(n, a_list, max_el=a_list[0][0], max_i=0, max_g=0, i=0, g=0):
                # знаходження індексу максимального елементу масиву рекурсивно
                if a_list[i][g] > max_el:
                    max_el = a_list[i][g]
                    # якщо поточний елемент більший за максимальний, записуємо його у змінну max_el
                    # (по замовчуванню у змінній перший елемент списку)
                    max_i = i  # стовпчик максимального елементу
                    max_g = g  # рядок максимального елементу

                # зімітуємо ітерацію лічильниками і (поточний стовпчик) та g (поточний рядок)
                # і збільшується з кожним кроком, а g переходить на наступний рядок лише тоді,
                # коли закінчить перебір усіх елементів поточного рядка
                if i == (n - 1):
                    i = -1
                    g += 1
                i += 1
                if g == n:
                    return max_el, (max_i, max_g)
                return maxindex_recur(n, a_list, max_el, max_i, max_g, i, g)

            def maxindex_iter(n, a_list, max_i = 0, max_g = 0):  # знаходження індексу максимального елементу масиву ітераційно
                max_el = a_list[0][0]
                for i in range(n):
                    for g in range(n):
                        if a_list[i][g] > max_el :
                            max_el = a_list[i][g]
                            max_i = i
                            max_g = g
                return max_el, (max_i, max_g)
                # принцип роботи ітераційної функції аналогічний до рекурсивної,
                # тільки замість лічильників використовуємо цикли


            start31 = datetime.now()
            time.sleep(1)
            num_maxindex_recur = maxindex_recur(n,a_list)
            end31 = datetime.now()
            start32 = datetime.now()
            time.sleep(1)
            num_maxindex_iter = maxindex_iter(n, a_list)
            end32 = datetime.now()

            print(f'Max element of array A and its index \nA:\n{a} : \nusing recursion {num_maxindex_recur} '
                  f'\n excecution time: {end31-start31}; '
                  f'\nusing iteration {num_maxindex_recur} \n excecution time: {end32-start32}.')

        else:
            print("\nError! Input '1', '2' or '3'.")
            continue
        break

    answer = input('\nDo you want to continue? Yes-1, No-2:')
    if answer == '1':
        continue
    else:
        break