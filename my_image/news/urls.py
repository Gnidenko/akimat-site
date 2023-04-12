from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]