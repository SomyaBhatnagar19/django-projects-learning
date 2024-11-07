#creating urls to store the app views 
from django.urls import path
from . import views


urlpatterns = [
    path('sports/', views.sports_view),
    path('finance/', views.finance_view),
    path('politics/', views.politics_view)
]