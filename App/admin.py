from django.contrib import admin

from .models import Address, Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ('excerpt', )

    def excerpt(self, obj):
        return obj.get_excerpt(4)

admin.site.register(Address)
admin.site.register(Restaurant, RestaurantAdmin)
