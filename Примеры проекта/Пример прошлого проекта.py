from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.db import connection

def server_bd (requst):

    a = requst.POST.get('delete')
    b = requst.POST.get('BBB')

    name = requst.POST.get('name', "")
    age = requst.POST.get('age', "")
    gender = requst.POST.get('gender', "")
    filter = requst.POST.get('filter', "")

    gg=""
    table = ""
    if filter == "filter":
        filter = f'where name like "{filter}%"'


    with connection.cursor() as cursor:
        if a == "delete":
            cursor.execute("delete  from new_mohito_app_Person")
        else:
            if name and age and gender:

                cursor.execute(f"insert into new_mohito_app_Person (name,age ,gender) values ('{name}','{age}','{gender}')")

            cursor.execute(f"select * from new_mohito_app_Person {filter} order by name desc")

            rowss = cursor.fetchall()  # получаем все строки


            for row in rowss:

                table += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>\n\r'


    data ={"massage":f'a = "{a} b = {b}"',
           "BD":f"имя - '{name}' возраст - '{age}'  пол - '{gender}'",
           "table": table
           }


    return render(requst, "faice.html", context=data)


def info_bd (requst):


    table = ""


    with connection.cursor() as cursor:

        cursor.execute(f"select * from new_mohito_app_Person  order by name desc")

        rowss = cursor.fetchall()  # получаем все строки

        for row in rowss:
            table += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>\n\r'

    data = {
            "table": table
            }
    return render(requst, "dva.html", context=data)


def index(params):
    a = "привет"
    data = {"massage": a}
    # получаем из строки запроса имя пользователя
    result = ''
    a = params.POST.get("a_chislo", "")
    b = params.POST.get("b_chislo", '')
    if a != "" and b != "":

        a = int(a)
        b = int(b)

        x = []
        langs = params.POST.getlist("languages", [])
        x.append(langs)

        result = 0

        if "+" in x[0]:
            result = a + b

        if "-" in x[0]:
            result = a - b

        if "*" in x[0]:
            result = a * b

        if "/" in x[0]:
            if b == 0:
                result = 'на ноль делиь нельзя'
            else:
                result = a / b
    data = {"massage": result}

    return render(params, "index.html", context=data)


