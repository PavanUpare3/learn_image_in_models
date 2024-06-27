from django.contrib import admin

from .models import MyModel

@admin.register(MyModel)

class imageAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'image')

