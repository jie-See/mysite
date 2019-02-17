from django.urls import path
from . import views

app_name = 'app_name'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('bad/', views.current_url_view_bad,),
    path('good/', views.current_url_view_good,),
    path('display_bad/', views.ua_display_bad),
    path('search-form/', views.search_form),
    path('search/', views.search)
]
