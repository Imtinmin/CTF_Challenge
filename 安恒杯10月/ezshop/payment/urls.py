from django.urls import path
from .views import checkPayment
app_name='payment'
urlpatterns = [
	path('check', checkPayment, name='check')
]