from django.contrib import admin
from home.models import *

# admin.site.register(FirstTable)

admin.site.site_header = "Gaurav Admin"
admin.site.site_title = "K"
admin.site.site_url = "Expense Tracker"

# customizing the admin interface
class CustomAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "age",
        "phone"
    ]

# add the search field, list filter, ordering 
    search_fields = ['name', 'email']  # can take multiple value for make seacrh regarding that
    list_filter = ['age']  # take multiple field make fillter regarding that
    ordering = ['-phone']  #


admin.site.register(FirstTable, CustomAdmin)

# Implementing Search_fields, filters and ordering in the admin Panel