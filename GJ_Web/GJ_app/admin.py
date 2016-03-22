from django.contrib import admin
from .models import *
# Register your models here.

class Userdisplay(admin.ModelAdmin):
    list_display = ('user_id', 'company_name', 'email', 'is_admin')

class Branchdisplay(admin.ModelAdmin):
    list_display = ('branch_id', 'company_id', 'branch_phone', 'branch_address', 'branch_city', 'branch_state', 'branch_zipcode', 'date_added')

class Categorydisplay(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')

class Optiondisplay(admin.ModelAdmin):
    list_display = ('option_id', 'option_name')

class CategoryOptiondisplay(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'option_id')

class Companydisplay(admin.ModelAdmin):
    list_display = ('id', 'company_id', 'company_name', 'main_phone', 'main_address', 'main_city', 'main_state', 'main_zipcode', 'date_created', 'last_updated')

class Containerdisplay(admin.ModelAdmin):
    list_display = ('container_id', 'container_name')

class Sizedisplay(admin.ModelAdmin):
    list_display = ('size_id', 'size_name')

class Itemdisplay(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'category_id', 'container_id', 'options', 'options_isFixed', 'options_price', 'item_mealOptions', 'item_mealPrice')

class Menudisplay(admin.ModelAdmin):
	list_display = ('item_id', 'menu_id', 'item_nickname', 'item_basePrice', 'item_isActive', 'item_startDate', 'item_endDate', 'item_startTime', 'item_endTime')

class ItemSizedisplay(admin.ModelAdmin):
	list_display = ('id', 'item_id', 'size_id', 'itemSizePrice', 'item_count')


admin.site.register(User, Userdisplay)
admin.site.register(Branch, Branchdisplay)
admin.site.register(Category, Categorydisplay)
admin.site.register(Option, Optiondisplay)
admin.site.register(CategoryOption, CategoryOptiondisplay)
admin.site.register(Company, Companydisplay)
admin.site.register(Container, Containerdisplay)
admin.site.register(Menu, Menudisplay)
admin.site.register(Size, Sizedisplay)
admin.site.register(Item, Itemdisplay)
admin.site.register(ItemSize, ItemSizedisplay)
