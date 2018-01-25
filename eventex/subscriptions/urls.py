from django.conf.urls import url

from eventex.subscriptions.views import new, detail

urlpatterns = [
    url(r'^([0-9A-Fa-f-]+)/$', detail, name='detail'),
    url(r'^$', new, name='new'),
]
