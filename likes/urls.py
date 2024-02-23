from django.urls import path
from likes import views


urlpatterns = [
    path('', views.LikesList.as_view()),
]
