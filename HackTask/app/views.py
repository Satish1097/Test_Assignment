from django.shortcuts import render,redirect,HttpResponse
from .models import User,Task
from django.core.paginator import Paginator
import openpyxl


def home(request):
    return render(request,'index.html')

def AddUser(request):
    if request.method=="GET":
        return render(request,'Adduser.html')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('phone')

        data=User(name=name,email=email,mobile=mobile)
        data.save()
        return redirect('/UserList')

def AddTask(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        taskdetail = request.POST.get('task_detail')
        tasktype = request.POST.get('task_type')
        Task.objects.create(user_id=user_id, taskdetail=taskdetail, tasktype=tasktype)
        return redirect('/TaskList')
    else:
        users = User.objects.all()
        return render(request, 'addtask.html', {'users': users})
        
    
def UserList(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)
    pg_number = request.GET.get('page')
    page_data = paginator.get_page(pg_number)
    return render(request, 'UserList.html', {'page_data': page_data})

def TaskList(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 10)
    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)
    return render(request, 'TaskList.html', {'page_data': page_data})

def exportExcel(request):
    tasks = Task.objects.all()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tasks"
    ws.append(["User Name", "Task Detail", "Task Type"])

    for task in tasks:
        user_name = task.user.name if task.user else "N/A"
        ws.append([user_name, task.task_detail, task.task_type])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=tasks.xlsx'
    wb.save(response)
    return response