from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^translate/',views.translate,name='translate'),
    url(r'^about/',views.about,name='AboutUs'),
]

