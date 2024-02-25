from django.urls import path
from passions import views

urlpatterns = [
    path('', views.PassionList.as_view()),
    path('<int:pk>/', views.PassionDetail.as_view()),
]
