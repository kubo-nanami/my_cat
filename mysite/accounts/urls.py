from django.urls import path
from . import views
from mysite import settings


app_name = "accounts"
urlpatterns = [
    path('signup/', views.SignUpView.as_view(templatename="account/signup.html"), name='signup'),
    path('login/', views.LoginView.as_view(templatename="account/login.html"), name='login'),
    path('logout/', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
