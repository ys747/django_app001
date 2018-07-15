# -*- coding: utf-8 -*-

"""
Created on Sat Jun 30 16:11:18 2018

@author: blueb
"""
from django.urls import path
#from django.conf.urls import url
#from .views import HelloView
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('find/', views.find, name='find'),
    #url(r'', HelloView.as_view(), name='index'),
    #path('form', views.form, name='form'),
    #path('<int:id>/<nickname>/', views.index, name='index'),
]
