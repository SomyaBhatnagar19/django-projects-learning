#creating urls to store the app views 
from django.urls import path
from . import views


urlpatterns = [
    # making dynamic urls for views
    path('<str:topic>/', views.news_view),
     path('<int:num1>/<int:num2>/', views.add_view),
]