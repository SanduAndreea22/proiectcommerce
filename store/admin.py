from django.contrib import admin
from .models import Parfum

@admin.register(Parfum)
class ParfumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


