from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from portal.models import Category, Redactor, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "published_date"]
    list_filter = ["publishers"]
    search_fields = ["title"]


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Info", {"fields": (
            "first_name",
            "last_name",
            "years_of_experience")}),)


admin.site.register(Category)
admin.site.unregister(Group)
