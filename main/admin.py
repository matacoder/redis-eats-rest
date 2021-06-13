from django.contrib import admin
from main.models import User, Dish


class UserAdmin(admin.ModelAdmin):
    pass


class DishAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dish, DishAdmin)
admin.site.register(User, UserAdmin)
