import cgi
import sys
import random
import cgitb
import random
import pickle

cgitb.enable()
sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')

max_test = 3


def get_test(file_name):
    _f = open(file_name, 'rb')
    test_list = pickle.load(_f)
    _f.close()
    _test = random.choice(test_list)
    test_list.remove(_test)
    _f = open('cur_tests.dat', 'wb')
    pickle.dump(test_list, _f)
    _f.close()
    return _test


def write_results(_user_dict, out_points=0, out_tests=0, out_answers=0):
    print('<i><b>Результаты тестирования:</b></i>',
          '<br>Имя &ndash; ', _user_dict['name'])
    if out_points:
        print('<br>Получено баллов &ndash; ',
              _user_dict['points'], ' из ', _user_dict['number_test'])
    if out_tests:
        print('<br>Тесты &ndash; ')
        for el in _user_dict['tests']:
            print(el.split('.')[0])
    if out_answers:
        print('<br>Ответы &ndash; ')
    for el in _user_dict['answers']:
        print(el)
    print('<br>Оценка &ndash; ')
    m = _user_dict['points']
    if m == 0:
        mark = "Неудовлетворительно"
    elif m == 1:
        mark = "Удовлетворительно"
    elif m == 2:
        mark = "Хорошо"
    else:
        mark = "Отлично"
    print('"', mark, '"')


data = cgi.parse()
flag = True
if 'answer' not in data.keys():
    print('Имя: ', data['name'][0])
    print('<br/>')
    test = get_test('tests.dat')
    print(test)
    user_dict = {
        'name': data['name'][0],
        'number_test': 1,
        'tests': [test],
        'answers': [],
        'points': 0}
    f = open('user.dat', 'wb')
    pickle.dump(user_dict, f)
    f.close()
else:
    f = open('user.dat', 'rb')
    user_dict = pickle.load(f)
    f.close()
    if user_dict['number_test'] <= max_test:
        user_dict['answers'] += [data['answer'][0]]
    if user_dict['number_test'] == max_test:
        write_results(user_dict, out_points=1, out_tests=1, out_answers=1)
    else:
        tests = user_dict['tests']
        etalon = tests[len(tests) - 1:][0].split(';')[1]
        if data['answer'][0] == etalon:
            user_dict['points'] += 1
        test = get_test('cur_tests.dat')
        print(test)
        user_dict['number_test'] += 1
        user_dict['tests'] += [test]
        f = open('user.dat', 'wb')
        pickle.dump(user_dict, f)
        f.close()
