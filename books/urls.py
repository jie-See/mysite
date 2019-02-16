from django.urls import path
from . import views

app_name = 'app_name'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('bad/', views.current_url_view_bad,),
    path('good/', views.current_url_view_good,),
]
