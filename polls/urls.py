from django.urls import path

from polls.views import index, ola
from polls import views

urlpatterns = [
    path('index/', index,name='index'),
    path('ola/', ola, name='ola'),
    path('enquete/<int:pk>/show/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('enquete/list/', views.QuestionListView.as_view(), name='polls_list'),
]
