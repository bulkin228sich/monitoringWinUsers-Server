from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http.response import JsonResponse


conn = mysql.connector.connect(
    host="localhost",
    database="controlempl",
    user="root",
    password="" )
cursor = conn.cursor(buffered=True)

def home(request):
    return render(request, 'app/index.html')

@csrf_exempt
def info(request):
    print("1")
    if request.method == 'POST':
        print("2")
        
        
        name = request.POST.get('name')
        print(name)
        domain = request.POST.get('domain')
        print(domain)
        machine = request.POST.get('machine')
        print(machine)
        ip = request.POST.get('ip')
        print(ip)
        time = str(datetime.now().time()).split('.')[0]
        print(time)
        cursor.execute('''SELECT name FROM empl WHERE  name = %s ''', (name, ))
        if len(cursor.fetchall()):
            query = 'UPDATE empl SET domain = %s, machine = %s, ip= %s , time = %s WHERE name = %s'                 
            cursor.execute(query, (domain,machine, ip, time,  name))
            conn.commit() 
        else:
            query = """INSERT INTO `empl` (`id`, `name`, `domain`, `machine`, `ip`, `time`) 
            values (null, %s,  %s, %s, %s, %s);"""
            cursor.execute(query, (name, domain, machine, ip, time))
            conn.commit()
            
    return HttpResponse(status=204)

def userInfo(request):
    cursor.execute('''SELECT * FROM empl ''')
    info = cursor.fetchall()
    return JsonResponse(info , safe=False)