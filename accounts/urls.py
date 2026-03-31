from django.urls import path

from accounts import views

urlpatterns = [
    path(
        'account/signup',
        views.AccountCreateView.as_view(),
        name='signup'
    ),
    path(
        'account/profile',
        views.AccountTemplateView.as_view(),
        name='account_detail'
    )
]