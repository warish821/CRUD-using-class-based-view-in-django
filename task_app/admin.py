from django.contrib import admin

from task_app.models import Users, Task

# Register your models here.
admin.site.register(Users)
admin.site.register(Task)
