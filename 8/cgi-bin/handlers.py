import cgi
import sys
import re

main_form = cgi.FieldStorage()
sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')

data1 = (main_form.getfirst('data1') or '').strip()
data2 = (main_form.getfirst('data2') or '').strip()
data3 = (main_form.getfirst('data3') or '').strip()
data4 = (main_form.getfirst('data4') or '').strip()

results = [re.compile(r'^факультет - ([a-zA-Za-яА-Я0-9]+) груп\. ([a-zA-Za-яА-Я0-9]+)$').match(data1),
           re.compile(r'^Фамилия И\.О\. [a-zA-Za-яА-Я0-9]+ [a-яА-Я]\.[a-яА-Я]\.$').search(data2),
           re.match(r'^ЗК № (\d{7})$', data3),
           re.search(r'^range(\s*)\(((\s*)(\d+)(\s*))((\)$)|(,(\s*)(\d+)(\s*),(\s*)(\d+)(\s*)\)$))', data4)]

for i, res in enumerate(results):
    print(f'data{i + 1} {"" if res else "не "}соответствует шаблону')
    print('<br>')
    print('<br>')

# факультет - форавор груп. авипвравггав75484
# Фамилия И.О. аворрво и.п.
# ЗК № 1234567
# range  (  12, 443  ,  43434)
