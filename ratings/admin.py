from django.contrib import admin
from .models import Module, ModuleInstance, ModuleLeaders, Professors, Ratings
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Module)
admin.site.register(ModuleLeaders)
admin.site.register(ModuleInstance)
admin.site.register(Professors)
admin.site.register(Ratings)