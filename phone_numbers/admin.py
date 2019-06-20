from django.contrib import admin
from .models import *


class NumbersAdmin(admin.ModelAdmin):
    exclude = ['']
    #list_filter = ['number']
    search_fields = ['who_call', ]


class NamesAdmin(admin.ModelAdmin):
    exclude = ['']
    # list_filter = ['numbers']
    search_fields = ['name', ]


admin.site.register(Numbers, NumbersAdmin)
admin.site.register(Names, NamesAdmin)