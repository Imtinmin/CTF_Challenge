from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .settings import LOGIN_REDIRECT_URL

urlpatterns = [
	path('', RedirectView.as_view(url=LOGIN_REDIRECT_URL), name='site-root'),
    path('admin-do-not-expose/', admin.site.urls),
	path('payment/', include('payment.urls', namespace='payment')),
	path('account/', include('account.urls', namespace='account')),
	path('shop/', include('shop.urls', namespace='shop')),
]
