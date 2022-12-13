import cgi
import sys

main_form = cgi.FieldStorage()
sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')


def form_post():
    # принимаем данные из формы
    in_name = main_form.getfirst("in_name")
    in_university = main_form.getfirst("in_university")
    in_phone = main_form.getfirst("in_phone")

    return in_name, in_university, in_phone


print(form_post())
