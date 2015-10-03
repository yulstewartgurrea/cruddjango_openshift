from django.contrib import admin

# Register your models here.

from crudapp.models import User

admin.site.register(User)