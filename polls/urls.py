from django.urls import path

from polls.views import index, ola
from polls import views

urlpatterns = [
    path('', index,name='index'),
    path('ola/', ola, name='ola'),
    path('enquete/<int:pk>/show/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('enquete/list/', views.QuestionListView.as_view(), name='polls_list'),
    path('enquete/<int:question_id>/vote/', views.vote, name='poll_vote'),
    path('enquete/<int:question_id>/results/', views.results, name='poll_results'),
]
