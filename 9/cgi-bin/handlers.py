import cgi
import sys
import random


main_form = cgi.FieldStorage()
sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')

name = (main_form.getfirst('data1') or '').strip()
func1_flag = main_form.getfirst('data2')
func2_flag = main_form.getfirst('data3')
func3_flag = main_form.getfirst('data4')

numbers = [random.randint(-20, 5) for _ in range(7)]


def func1(nmb):
    res = 1
    for n in nmb:
        res *= abs(n)
    return res


def func2(nmb):
    return abs(min(nmb, key=abs))


def func3(nmb):
    return list(map(abs, sorted(nmb, key=abs)))


print('Имя: ', name)
print('<br/>')
print('Числа: ', numbers)
print('<br/>')
print('Произведение чисел, взятых по абсолютной величине',
      func1(numbers) if func1_flag == 'on' else 'не считалось')
print('<br/>')
print('Минимальное число среди чисел, взятых по абсолютной величине',
      func2(numbers) if func2_flag == 'on' else 'не находилось')
print('<br/>')
print('Сортировка чисел, взятых по абсолютной величине',
      func3(numbers) if func3_flag == 'on' else 'не выполнялась')
print('<br/>')
