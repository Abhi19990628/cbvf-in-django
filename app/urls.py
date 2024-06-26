from django.urls import path
from .views import InformationList, InformationDetail,Studentinformation,collagesinformations,StudentDetails,TeacherInformations,principalinfromation
urlpatterns = [
    path('info/', InformationList.as_view(), name='informations-list'),
    path('info/<int:pk>/', InformationDetail.as_view(), name='informations-detail'),
    path('infos',Studentinformation.as_view(), name='Studentinfromation'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='student-details'),
    path('infoc',collagesinformations.as_view(),name ='collagesinformations'),
    path('infot', TeacherInformations.as_view(), name= 'teachersinformations'),
    path('infop', principalinfromation.as_view() ,name='informationabout principals'),
    path('infot', TeacherInformations.as_view(), name= 'teachersinformations'),
    path('infop', principalinfromation.as_view() ,name='informationabout principals')
    

]
