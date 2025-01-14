from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('<str:image_id>/', views.image_detail, name='image_detail'),
]
