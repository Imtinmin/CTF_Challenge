from django.urls import path
from .views import shopIndexView, createOrderView, myOrderView, cancelOrder, payOrder, cleanCanceledOrder

app_name='shop'
urlpatterns = [
	path('', shopIndexView, name='index'),
	path('createOrder/<int:goodid>', createOrderView, name='createOrder'),
	path('myOrder', myOrderView, name='myOrder'),
	path('cancelOrder/<int:orderid>', cancelOrder, name='cancelOrder'),
	path('payOrder/<int:orderid>', payOrder, name='payOrder'),
	path('cleanCanceledOrder', cleanCanceledOrder, name='cleanCanceledOrder')
]
