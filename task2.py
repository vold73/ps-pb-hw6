def FizzBuzz (num):
# Если число num делится на 3, то выводим Fizz, если на 5, то Buzz, если на 3 и на 5, то FizzBuzz
    if num % 3 == 0 and num % 5 == 0:
       return 'FizzBuzz'
    elif num % 5 == 0:
       return 'Buzz'
    elif num % 3 == 0:
       return 'Fizz'
    return ''

sum = 0
for i in range (1000, 20001):
    if FizzBuzz(i) == 'FizzBuzz':
       sum += i

print(f'Сумма чисел от 1000 до 20000 которые делятся на 3 и на 5 - {sum}')
        