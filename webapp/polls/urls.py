from django.urls import path

from . import views
urlpatterns = [
                path('index', views.index, name="polls"),
                # ex: http://127.0.0.1:8000/polls/

                # ex: http://127.0.0.1:8000/polls/5/
                path('<int:question_id>/', views.detail, name='detail'),

                # ex: http://127.0.0.1:8000/polls/5/results/
                path('<int:question_id>/results/', views.results, name='results'),

                # ex: http://127.0.0.1:8000/polls/5/vote/
                path('<int:question_id>/vote/', views.vote, name='vote'),
                
                #http:127.0.0.1:8000/polls/sample
                path('', views.sample, name='sample'),
                
                path('sample1/', views.sample1, name='sample1'),
                
                path('sample2/', views.sample2, name='sample2'),
 ]

