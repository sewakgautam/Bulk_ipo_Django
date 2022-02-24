from distutils.command import register
from django.contrib import admin

from apply.models import AddAccount

# Register your models here.


admin.site.register(AddAccount)
