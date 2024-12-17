from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited')
    search_fields = ('title',)
    list_filter = ('buyer',)
    list_per_page = 2
    fieldsets = (
        (None, {
            'fields': ('title', 'cost', 'size', 'description',)
        }),
        ('Дополнительные сведения:', {
            'classes': ('collapse',),
            'fields': ('buyer', 'age_limited',)
        }),
    )
    readonly_fields = ('age_limited',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date',)
    search_fields = ('title',)