from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app2_index'),
    path('page1/', views.page1, name='app2_page1'),
    path('page2/', views.page2, name='app2_page2'),
]
