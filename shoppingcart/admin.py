from django.contrib import admin

from .models import Category, Product, ShoppedItemList


class CategoryAdminView(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('id','category_name',)
    list_display_links = ('category_name','id',)
    ordering = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)
    filter_horizontal = ()
    fieldsets = (
        ('User Information', {
            'fields': ('category_name','slug',),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Category, CategoryAdminView)


class ProductAdminView(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'id',)
    list_display_links = ('product_name',)
    ordering = ('-product_name',)
    list_filter = ('product_name',)
    search_fields = ('product_name',)
    filter_horizontal = ()
    fieldsets = (
        ('User Information', {
            'fields': ('product_name','slug',),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Product, ProductAdminView)


class ShoppedItemListAdminView(admin.ModelAdmin):
    list_display = ('user', 'id',)
    list_display_links = ('user',)
    ordering = ('-user',)
    list_filter = ('user',)
    search_fields = ('user',)
    filter_horizontal = ()
    fieldsets = (
        ('User Information', {
            'fields': ('user',),
            'classes': ('collapse',),
        }),
    )


admin.site.register(ShoppedItemList, ShoppedItemListAdminView)

