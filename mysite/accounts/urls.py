from django.urls import path
from . import views
from mysite import settings


app_name = "accounts"
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]