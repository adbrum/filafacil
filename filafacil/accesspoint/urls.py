from django.conf.urls import url
from filafacil.accesspoint.views import new

urlpatterns = [
    url(r'^$', new, name='new'),

]