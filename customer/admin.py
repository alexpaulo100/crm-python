from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "firt_name", "last_name", "email"]
# Register your models here.
