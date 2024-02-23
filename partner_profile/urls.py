from django.urls import path
from partner_profile import views

urlpatterns = [
    path('', views.PartnerProfileList.as_view()),
    path('<int:pk>/', views.PartnerProfileDetail.as_view()),
]
