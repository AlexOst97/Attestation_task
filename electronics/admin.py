from django.contrib import admin
from electronics.models import Contacts, Product, Network


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number', 'created_at')
    list_filter = ('country', 'city')
    search_fields = ('email', 'country', 'city', 'street')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    list_filter = ('release_date',)
    search_fields = ('name', 'model')


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'contacts', 'products_list', 'supplier_get', 'created_at', 'arrears')
    list_filter = ('type', 'contacts__city')
    search_fields = ('name', 'contacts__city')

    def products_list(self, obj):
        products = obj.product.all().values_list('name', flat=True)
        return ", ".join(products)
    products_list.short_description = 'Продукты'

    def supplier_get(self, obj):
        if obj.supplier:
            return obj.supplier.name
        else:
            return "Нет поставщика"
    supplier_get.short_description = 'Поставщик'

    def clear_arrears(self, queryset):
        queryset.update(debt=0)
    clear_arrears.short_description = "Очистить задолженность"