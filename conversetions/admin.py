from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Conversation)
class ConverationAdmin(admin.ModelAdmin):
    list_display = ['__str__', "count_messages", 'count_participants']


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', "created"]