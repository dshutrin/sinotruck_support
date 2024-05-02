from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CustomUser)
class Admin(admin.ModelAdmin):
    list_display = ('username', )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
