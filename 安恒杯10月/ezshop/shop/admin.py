from django.contrib import admin
from .models import Good, Order
# Register your models here.

class GoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'amount', 'available')
admin.site.register(Good, GoodAdmin)

class OrderAdmin(admin.ModelAdmin):
	pass
admin.site.register(Order, OrderAdmin)