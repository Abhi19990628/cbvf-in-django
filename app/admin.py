from django.contrib import admin
from .models import Informations,Student,Collages,Teacher,principal

@admin.register(Informations)

class userinformations(admin.ModelAdmin):
    list_display = ['id','name','email','phone','text']

@admin.register(Student)
class userstudent(admin.ModelAdmin):
    list_display = ['name', 'roll' ,'des']
    
    
@admin.register(Collages)
class detailscollages (admin.ModelAdmin):
    list_display =['name','collage_no','city','iet_no']


@admin.register(Teacher)
class detailsTeacher(admin.ModelAdmin):
    list_display =['name','subject','age']
    
@admin.register(principal)
class detailsprincipal(admin.ModelAdmin):
    list_display = [ 'name', 'class_room', 'age', 'subject']