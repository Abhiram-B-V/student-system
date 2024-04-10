from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/',views.signup,name='signup_url'),
    path('login/',views.login,name='login_url')
]