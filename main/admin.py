from django.contrib import admin

from main.models import (
    Cashflow,
    Dish,
    DishDateLink,
    Transaction,
    User,
    MainSwitch,
    DishType,
    IngredientType,
    Supplier,
    Ingredient,
)


class UserAdmin(admin.ModelAdmin):
    pass


class DishAdmin(admin.ModelAdmin):
    pass


class DishDateLinkAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


class CashflowAdmin(admin.ModelAdmin):
    pass


class DishTypeAdmin(admin.ModelAdmin):
    pass


class IngredientTypeAdmin(admin.ModelAdmin):
    pass


class SupplierAdmin(admin.ModelAdmin):
    pass


class MainSwitchAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dish, DishAdmin)
admin.site.register(DishDateLink, DishAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(MainSwitch, CashflowAdmin)
admin.site.register(DishType, CashflowAdmin)
admin.site.register(IngredientType, CashflowAdmin)
admin.site.register(Supplier, CashflowAdmin)
admin.site.register(Ingredient, CashflowAdmin)
