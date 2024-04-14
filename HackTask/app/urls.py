from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('AddUser/',views.AddUser),
    path('AddTask/',views.AddTask),
    path('UserList/',views.UserList),
    path('TaskList/',views.TaskList),
    path('exportExcels',views.exportExcel) 
]