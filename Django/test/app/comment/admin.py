from django.contrib import admin
from .models import *
# Register your models here.

admin.register(comment)


# from django.contrib import admin
# from .models import *
# from application.models import *
# from person.models import *

# class CommentInline(admin.TabularInline):
#     model = comment
#     extra = 1

# @admin.register(person)
# class PersonAdmin(admin.ModelAdmin):
#     inlines = [CommentInline]

# @admin.register(application)
# class ApplicationAdmin(admin.ModelAdmin):
#     inlines = [CommentInline]