from django.contrib import admin
from .models import Write 

# Register your models here.
class WriteAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Write, WriteAdmin)