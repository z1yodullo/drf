from django.urls import path
from .views import *

urlpatterns=[
    path('',tea_list),
    path('get_teacher_by_id/<int:pk>/',get_tea_by_id),
    path('update_teacher/<int:pk>/',update_tea),
    path('del_teacher/<int:pk>/',del_tea),
    path('courses',cour_list),
    path('get_courses_by_id/<int:pk>/',get_cour_by_id),
    path('update_courses/<int:pk>/',update_cour),
    path('del_courses/<int:pk>/',del_cour),
    path('students',stud_list),
    path('get_students_by_id/<int:pk>/',get_stud_by_id),
    path('update_students/<int:pk>/',update_stud),
    path('del_students/<int:pk>/',del_stud),
]