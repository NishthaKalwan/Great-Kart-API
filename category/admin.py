from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):

    # prepopulated_field: automatically fills in a field based on the value of another field.
    # It only autofills when creating a new object — not when editing an existing one.

    prepopulated_fields = {'slug': ('category_name',)}

    list_display        = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)



