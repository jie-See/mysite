from django.urls import path
from . import views

app_name='app_name'
urlpatterns = [

    path('', views.blog_title, name="blog_title"),

]
