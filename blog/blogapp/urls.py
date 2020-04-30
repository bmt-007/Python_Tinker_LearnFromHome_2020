from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index),
    path('blog/<slug>/', views.slug),
    path('dashboard/',views.dashboard),
    path('login/',views.login),
    path('dashboard/logout/',views.logout),
    path('dashboard/add', views.add),
    path('dashboard/delete', views.delete),
    path('dashboard/update/<id>/',views.update),
    path('dashboard/update/<id>/update',views.update),
    
    
]