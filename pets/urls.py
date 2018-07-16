from django.conf.urls import url
from . import views

#a map to our application


urlpatterns=[

    url(r'^$',views.index,name='index'),
    url(r'^add$',views.set_pet,name='add'),
    url(r'^contact$',views.contact,name='contact'),
    url(r'^about$',views.about,name='about')
]