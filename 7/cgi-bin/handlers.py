import cgi
import sys
import os

catalog = 'CGI'
if not os.path.isdir(f'./{catalog}'):
    os.mkdir(f'./{catalog}')
os.chdir(f'./{catalog}')

main_form = cgi.FieldStorage()
sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')

name_field = 'in_name'
university_filed = 'in_university'
phone_field = 'in_phone'

name = main_form.getfirst(name_field)
university = main_form.getfirst(university_filed)
phone = main_form.getfirst(phone_field)

with open('names.txt', 'w') as names_file:
    names_file.write(name_field + '\n')
    names_file.write(university_filed + '\n')
    names_file.write(phone_field + '\n')

with open('values.txt', 'w') as values_file:
    values_file.write(name or '' + '\n')
    values_file.write(university or '' + '\n')
    values_file.write(phone or '' + '\n')

names_file_size = os.path.getsize('names.txt')
values_file_size = os.path.getsize('values.txt')
print(f'Длина файла "names.txt": {names_file_size}')
print(f'Длина файла "values.txt": {values_file_size}')

with open('values.txt', 'r') as values_file:
    print(f'Содержимое файла "values.txt": {values_file.read()}')

sequence = bytes(range(25))
with open('binary_data.dat', 'wb') as binary_file:
    binary_file.write(sequence)

with open('binary_data.dat', 'rb') as binary_file:
    data = binary_file.read()
    print(f'Значение 20-го байта: {data[20]}')
    try:
        binary_file.seek(-4, 2)
        print(f'Значение трех байтов: {binary_file.read(3)}')
    except OSError:
        print('Недопустимые значения для "offset" и "whence"')

    digit = str(data[-1])[-1]
    try:
        assert digit == 3
        print(f'Последняя цифра {digit} в последнем числе последовательности совпадает с целевой')
    except AssertionError:
        print(f'Последняя цифра {digit} в последнем числе последовательности не совпадает с целевой')
