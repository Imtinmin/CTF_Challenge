from django.urls import path
from django.contrib.auth.views import login, logout
from .views import registerView

app_name='account'
urlpatterns = [
	path('login', login, {'template_name': 'account/login.html'}, name='login'),
	path('register', registerView, name='register'),
	path('logout', logout, {'next_page': 'shop:index'}, name='logout'),
]
