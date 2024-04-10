from django.urls import path

from . import views

urlpatterns = [
    path('home/',views.home_request,name='home_url'),
    path('about/',views.about),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('course/',views.course),
    path('single/',views.single),
    path('teacher/',views.teacher),
]
