from django.contrib import admin
from .models import Post,Student,Comment,Department

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "email"]

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "faculty", "noofstd"]
     
 
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Student,StudentAdmin)
admin.site.register(Department,DepartmentAdmin)