from django.contrib import admin
from home.models import *

# 01 admin.site.register(FirstTable)

admin.site.site_header = "Gaurav Admin"
admin.site.site_title = "K"
admin.site.site_url = "Expense Tracker"

# 04 Creating Custom Actions in Django Admin
@admin.action(description="testing purpose")
def cal_age(modeladmin, request, queryset):
    for q in queryset:
        obj = FirstTable.objects.get(id=q.id)
        if obj.age < 10 :
            obj.age = obj.age*10
            obj.save()
    queryset.update(email="done_age_modi")

def display(self, obj):
    if obj.age > 10:
        return "you are 10+"
    else : return "below 10"

#  02 customizing the admin interface
class CustomAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "age",
        "phone"
    ]

# 03 add the search field, list filter, ordering 
    search_fields = ['name', 'email']  # can take multiple value for make seacrh regarding that
    list_filter = ['age']  # take multiple field make fillter regarding that
    ordering = ['-phone']  #

# 02 ka part 
admin.site.register(FirstTable, CustomAdmin)
#04 remain part
actions = [cal_age]
