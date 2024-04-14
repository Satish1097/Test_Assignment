from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('Add_Task/',views.Add_Task),
    path('UserList/',views.UserList),
    path('TaskList/',views.TaskList), 
]