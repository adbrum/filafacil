from django.conf.urls import url
from filafacil.screening.views import new

urlpatterns = [
    url(r'^$', new, name='new'),

]