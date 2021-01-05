def fib(n):
# функция расчета числа Фиббоначи с использованием рекурсии, взято с сайта https://all-pyton.ru
    cur = 1
    if n > 2:
        cur = fib(n-1) + fib(n-2)
    return cur


i = 1
even_sum = 0

print('Вывод четных эллементов числа Фиббоначи')
print('    №     |   число  ')
print(' элемента | Фиббоначи')
print('----------|----------')


while fib(i) < 10000000:
    if fib(i) % 2 == 0:
        print(f'{str(i).ljust(10, " ")}|{str(fib(i)).rjust(10, " ")}')
        even_sum += fib(i)        
    i += 1

print(f'Сумма четных чисел Фиббоначи - {even_sum}')
print(f'Количество элементов - {i-1}')
print(f'Предпоследний элемент №{i-2} - число Фиббоначи {fib(i-2)}')
