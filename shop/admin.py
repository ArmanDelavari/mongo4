from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}   # slug roo az name por mikone


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)  # category ro be soorate zarre bin miare
    actions = ('make_available',)   # in be khatere tabeye paine

    def make_available(self, request, queryset):   # miad un action ro avaz mikone
        rows = queryset.update(available=True)
        self.message_user(request, f'{rows} updated')

    make_available.short_description = 'make all available'
