from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['accuracy','communication','cleanliness','location','check_in','rating_average']