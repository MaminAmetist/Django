from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_filter = ('balance', 'age')
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_filter = ('buyer', 'cost', 'size')
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('title', 'cost', 'size')
        }),
        ('Дополнительные сведения:', {
            'classes': ('collapse',),
            'fields': ('buyer', 'age_limited', 'description')
        }),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date',)
    search_fields = ('title',)
