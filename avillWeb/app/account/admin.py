from django.contrib import admin
from .models import Account, Type_Account, Photo, Estado, TypeEstado
# Register your models here.

admin.site.register(Account)
admin.site.register(Photo)
admin.site.register(Type_Account)
admin.site.register(Estado)
admin.site.register(TypeEstado)
