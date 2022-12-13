

from django.urls import path, include

#import view from app1
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('error', views.error, name='error'),

]