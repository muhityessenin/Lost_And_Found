from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import LostItem, FoundItem


@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "date_lost", "user")
    search_fields = ("name", "location")
    list_filter = ("date_lost",)
    actions = ["delete_selected"]

@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "date_found", "user")
    search_fields = ("name", "location")
    list_filter = ("date_found",)
    actions = ["delete_selected"]
