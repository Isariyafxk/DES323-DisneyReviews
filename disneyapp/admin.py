from django.contrib import admin
from disneyapp.models import *
# Register your models here.

@admin.register(DisneylandReview)
class Disneyadmin(admin.ModelAdmin):
    pass