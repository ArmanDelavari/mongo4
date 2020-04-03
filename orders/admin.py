from django.contrib import admin
from .models import *

# Register your models here.
class OrderItemInline(admin.TabularInline):   # be soorate table
    model = Order_item
    raw_id_fields = ('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'update', 'paid')
    list_filter = ('paid',)
    inlines = (OrderItemInline,)   # balaio midim edameye in


@admin.register(Copon)
class CoponAdmin(admin.ModelAdmin):
    list_display = ('code', 'valid_from', 'valid_to', 'discount', 'active')
    list_filter = ('active', 'valid_to', 'discount')
    search_fields = ('code',)