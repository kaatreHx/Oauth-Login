from django.urls import path, include
from allauth.account.views import LoginView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('accounts/', include('allauth.urls')), 
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('success/', TemplateView.as_view(template_name='login/success.html'), name='success'),
]
