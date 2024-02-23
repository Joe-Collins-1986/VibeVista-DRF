from django.urls import path
from characteristics import views


urlpatterns = [
    path('', views.CharacteristicList.as_view()),
]
