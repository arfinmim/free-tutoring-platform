from django.urls import path
from . import views

urlpatterns = [


    path('students/register/', views.student_register, name='student_register'),
    path('students/', views.student_list, name='student_list'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

path('tutors/register/', views.tutor_register, name='tutor_register'),
path('tutors/', views.tutor_list, name='tutor_list'),
path('tutors/edit/<int:id>/', views.edit_tutor, name='edit_tutor'),
path('tutors/delete/<int:id>/', views.delete_tutor, name='delete_tutor'),
path('tutors/contact/<int:id>/', views.contact_tutor, name='contact_tutor'),
path('messages/', views.message_list, name='message_list'),
]