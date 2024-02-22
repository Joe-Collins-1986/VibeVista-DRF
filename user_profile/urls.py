from django.urls import path
from user_profile import views

urlpatterns = [
    path('', views.UserProfileList.as_view()),
    path('<int:pk>/', views.UserProfileDetail.as_view()),
]
