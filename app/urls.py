from django.urls import path
from .views import InformationList, InformationDetail

urlpatterns = [
    path('info/', InformationList.as_view(), name='informations-list'),
    path('info/<int:pk>/', InformationDetail.as_view(), name='informations-detail'),
]
