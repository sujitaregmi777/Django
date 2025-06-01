from django.contrib import admin
from .models import *

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date','end_date', 'location', 'created_at')
    list_filter = ('start_date','end_date','location')
    search_fields = ('title', 'description','location', 'user_name')
    ordering = ('-start_date',)

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

# @admin.register(Details)
# class DetailsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'school_name', 'class_name', 'phone', 'gpa')
#     search_fields = ('name', 'school_name', 'phone', 'gpa')
#     ordering = ('name',)
#     inlines = [EducationInline, SkillInline]


