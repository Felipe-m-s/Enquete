from django.urls import path

from polls import views

urlpatterns = [
    # Path para a página inicial
    path('', views.index, name='index'),
    # Path para a página de início
    path('home/', views.home, name='home'),
    # Path para a página de sobre
    path('about/', views.about, name='about'),
    # Path para a página de detalhes da questão
    path('enquete/<int:question_id>/', views.vote, name='question_detail'),
    # Path para a página de lista de questões
    path('enquete/list/', views.QuestionListView.as_view(), name='polls_list'),
    # Path para a página de resultados da enquete
    path('enquete/results/', views.results_match, name='poll_results_match'),
]
