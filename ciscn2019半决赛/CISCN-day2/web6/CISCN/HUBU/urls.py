from django.conf.urls import url
from . import view, api

urlpatterns = [
    url(r'^api/add_paper$', api.add_paper, name='add_paper'),
    url(r'^api/get_token$', api.get_token_, name='get_token'),
    url(r'^api/send_paper$', api.send_paper, name='send_paper'),
    url(r'^[^(api/)]', view.show_paper, name='show_paper'),
]