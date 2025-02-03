from django.urls import path
from .views import SignUpView, SignInView

app_name = "registration"

urlpatterns = [
    path('', SignUpView.as_view(), name="signup"),
    path('signin/', SignInView.as_view(), name="signin"),
]
