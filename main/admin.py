from django.contrib import admin

from main.models import Cashflow, Dish, Transaction, User


class UserAdmin(admin.ModelAdmin):
    pass


class DishAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


class CashflowAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dish, DishAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Cashflow, CashflowAdmin)
