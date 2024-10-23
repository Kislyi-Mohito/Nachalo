from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
@login_required
def info_vb(requst):
    sms = 'Получено ?'
    knopka1 = requst.POST.get('dobavit')
    name = requst.POST.get('name',"")
    a = requst.
    last_name = requst.POST.get('lname',"")
    deportament = requst.POST.get('работа',"")
    price = requst.POST.get("зарплата", "")
    zapros = requst.POST.get("запрос", "")
    logoutp = requst.POST.get("logout", "")
    table = ''
    nameuser = ''

    # Получение групп текущего пользователя
    user_groups = requst.user.groups.all()

    # Получение имен групп
    group_names = [group.name for group in user_groups]
    chek = 0
    for i in group_names:
        if i == ('test'):
            chek = 1
    print(chek)
    if logoutp == 'logout':
        logout(requst)
    with connection.cursor() as cursor:
        if chek != 1:
            if name and last_name and deportament and price:
                cursor.execute(f"insert into auth_permission (content_type_id, codename ,name) values ('{last_name}','{deportament}',{price})")

        cursor.execute(f"select * from auth_permission")

        rowss = cursor.fetchall()  # получаем все строки


        for row in rowss:
            table += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>\n\r'


    if requst.user.is_authenticated:
        # Получение имени текущего пользователя
        username = requst.user.username
        nameuser = f"Имя текущего пользователя:, {username}"
    else:
        nameuser = "нет такого"



    data = {"sms": f'имя {name} фамилия {last_name} должность {deportament} зарплата {price}',
            "table": table,
            'username' : nameuser,
            'roll': group_names,
            'chek': chek
            }




    return render(requst, 'visualBAZA.html', context= data)



def login1(request):


    if request.method == "POST":
        print("hello world")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if request.user.is_authenticated:
            # Получение имени текущего пользователя
            username = request.user.username
            print("Имя текущего пользователя:", username)
        else:
            print("Пользователь не аутентифицирован")



        if user:
            login(request, user)
            return HttpResponse('you have login <a href="http://127.0.0.1:8000/">Перейти</a>')

        else:

            return HttpResponse("wrong password or username")
    else:
        return render(request, 'avtirizaciya.html')

