from django.urls import path
from .views import InformationList, InformationDetail,Studentinformation,collagesinformations,StudentDetails
urlpatterns = [
    path('info/', InformationList.as_view(), name='informations-list'),
    path('info/<int:pk>/', InformationDetail.as_view(), name='informations-detail'),
    path('infos',Studentinformation.as_view(), name='Studentinfromation'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='student-details'),
    path('infoc',collagesinformations.as_view(),name ='collagesinformations'),

]
