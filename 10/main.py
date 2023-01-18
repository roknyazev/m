from http.server import HTTPServer, CGIHTTPRequestHandler
import pickle

TESTS = ['Тест №1. Изменяемые типы данных:'
         '<br>1. кортеж<br> 2. словарь <br>3. строка;010',
         'Тест №2. Выполняется только чтение из текстового файла:'
         '<br>1. mode=\'\' <br>2. mode=\'r\' <br>3. mode=\'r+\';110',
         'Тест №3. Выполняется удаление существующего файла:'
         '<br>1. mode=\'w\' <br>2. mode=\'w+\' <br>3. mode=\'a\';100',
         'Тест №4.В качестве ключа словаря могут быть использованы:'
         '<br>1. кортежи <br>2. числа <br>3. строки;111',
         'Тест №5. Модуль mod имеет фукцию func(). При каком подключении модуля'
         'фукция func() будет непосредсвтвенно доступна программе?'
         '<br>1. import mod <br>2. from mod import func <br>3. from mod import *;011']

f = open('tests.dat', 'wb')
pickle.dump(TESTS, f)
f.close()


address = ('localhost', 8000)
srv = HTTPServer(address, CGIHTTPRequestHandler)
srv.serve_forever()
