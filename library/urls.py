from django.urls import path
from library import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('footer/', views.footer, name='footer'),

    path('admission/', views.admission, name='admission'),
    path('community/', views.community, name='community'),
    path('student_list/', views.student_list, name='student_list'),

    path('achivement/', views.achivement, name='achivement'),
    path('achivementDetails/', views.achivementDetails, name='achivementDetails'),
    path('studentDetails/', views.studentDetails, name='studentDetails'),
    path('newcollection/', views.newcollection, name='newcollection'),
    path('collectionDetails/', views.collectionDetails, name='collectionDetails'),

    path('write_review/', views.write_review, name='write_review'),
    path('review/create/', views.review_create, name='review_create'),
]