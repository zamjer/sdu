from django.urls import path
from app_account import views

app_name = "app_account"


urlpatterns = [
    path("signup/", views.SignUpPage.as_view(), name="signup"),
    path("signin/", views.SignInPage.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),
    
    path("forgot/", views.ForgotPasswordPage.as_view(), name="forgot"),
]
