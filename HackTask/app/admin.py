from django.contrib import admin
from .models import User, Task
from import_export.admin import ExportActionMixin
from import_export import fields, resources

class TaskResource(resources.ModelResource):
    user_id = fields.Field(attribute='user_id', column_name='User ID')
    user_name = fields.Field(attribute='user__name', column_name='User Name')

    class Meta:
        model = Task
        fields = ('user_id', 'user_name', 'taskdetail', 'tasktype')

class TaskAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TaskResource
    list_display = ['get_user_id', 'get_user_name', 'taskdetail', 'tasktype']

    def get_user_id(self, obj):
        return obj.user.id

    def get_user_name(self, obj):
        return obj.user.name

    get_user_id.short_description = 'User ID'
    get_user_name.short_description = 'User'

admin.site.register(User)
admin.site.register(Task, TaskAdmin)