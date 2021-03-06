from django.contrib import admin

from main.models import (
    Cashflow,
    Dish,
    DishDateLink,
    DishType,
    Ingredient,
    IngredientType,
    MainSwitch,
    Supplier,
    Transaction,
    User,
    IngredientAmount,
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


class IngredientAmountAdmin(admin.ModelAdmin):
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
admin.site.register(IngredientAmount, IngredientAmountAdmin)
admin.site.register(Cashflow, CashflowAdmin)
