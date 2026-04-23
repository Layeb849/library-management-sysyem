from django.urls import path
from library import views 
urlpatterns = [

    path('', views.home, name='home'),
    path('pathagar/contact/', views.contact, name='contact'),
    path('pathagar/about/', views.about, name='about'),
    path('pathagar/service/', views.service, name='service'),
    path('pathagar/footer/', views.footer, name='footer'),

    path('pathagar/community/', views.community_view, name='community'),

    path('pathagar/achivement/', views.achivement, name='achivement'),
    # path('pathagar/achivementDetails/', views.achivementDetails, name='achivementDetails'),
    # path('pathagar/studentDetails/', views.studentDetails, name='studentDetails'),
    # path('pathagar/newcollection/', views.newcollection, name='newcollection'),
    # path('pathagar/collectionDetails/', views.collectionDetails, name='collectionDetails'),

    path('pathagar/write_review/', views.write_review, name='write_review'),
    path('pathagar/preview/create/', views.review_create, name='review_create'),

    path('pathagar/add_achievement/', views.add_yearly_achievement, name='add_yearly_achievement'),

    path('pathagar/committee/', views.upload_committee, name='committee'),

 #  Student Registration
    path('pathagar/register/', views.student_registration, name='student_registration'),

    path('pathagar/pending/', views.pending_list, name='pending_list'),

    path('pathagar/approve/<int:pk>/', views.approve_student, name='approve_student'),

    path('pathagar/reject/<int:pk>/', views.reject_student, name='reject_student'),

    path('pathagar/students/', views.student_list, name='student_list'),

    path('pathagar/student/profile/<int:pk>/', views.student_detail, name='student_detail'),



    path('pathagar/book/collection/', views.book_list, name='book_list'),

    path('pathagar/book/details/<int:pk>/', views.book_detail, name='book_detail'),

    path('pathagar/upload/book/', views.add_book, name='add_book'),
    
]