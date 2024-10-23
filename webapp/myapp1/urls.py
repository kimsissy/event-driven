from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app1_index'),
    path('page1/', views.page1, name='app1_page1'),
    path('page2/', views.page2, name='app1_page2'),
]
