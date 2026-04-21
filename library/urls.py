from django.urls import path
from library import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('footer/', views.footer, name='footer'),

    # path('admission/', views.admission, name='admission'),
    path('community/', views.community_view, name='community'),
    # path('student_list/', views.student_list, name='student_list'),

    path('achivement/', views.achivement, name='achivement'),
    path('achivementDetails/', views.achivementDetails, name='achivementDetails'),
    path('studentDetails/', views.studentDetails, name='studentDetails'),
    path('newcollection/', views.newcollection, name='newcollection'),
    path('collectionDetails/', views.collectionDetails, name='collectionDetails'),

    path('write_review/', views.write_review, name='write_review'),
    path('review/create/', views.review_create, name='review_create'),

    path('add_achievement/', views.add_yearly_achievement, name='add_yearly_achievement'),

    path('committee/', views.upload_committee, name='committee'),




    # membership urls
    # path('register/', views.student_registration, name='student_registration'),
    # path('students/', views.student_list, name='student_list'),
    # path('student/<int:pk>/', views.student_detail, name='student_detail'),



 # 🟢 1. Student Registration
    path('register/', views.student_registration, name='student_registration'),

    # 🟡 2. Pending List (Admin)
    path('pending/', views.pending_list, name='pending_list'),

    # ✅ 3. Approve Student
    path('approve/<int:pk>/', views.approve_student, name='approve_student'),

    # ❌ 4. Reject Student
    path('reject/<int:pk>/', views.reject_student, name='reject_student'),

    # 🟢 5. Approved Members List
    path('students/', views.student_list, name='student_list'),

    # 🔍 6. Student Detail
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
]