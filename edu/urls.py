from django.urls import path
from . import views
urlpatterns = [
    path('', views.NoteList.as_view(), name='NoteList'),
    path('<int:pk>/', views.NoteRetrieve.as_view(), name='NoteRetrieve'),
    path('<int:pk>/NoteDestroy', views.NoteDestroy.as_view(), name='NoteDestroy'),
    path('<int:pk>/NoteUpdate', views.NoteUpdate.as_view(), name='NoteUpdate'),
    path('<int:pk>/NoteRetUp', views.NoteRetUp.as_view(), name='NoteRetUp'),
    path('NoteCreate', views.NoteCreate.as_view(), name='NoteCreate'),
    path('StudentAddCreate', views.StudentAddCreate.as_view(),
         name='StudentAddCreate'),
    path('StudentAddList', views.StudentAddList.as_view(), name='StudentAddList'),
    path('FeedbackList', views.FeedbackList.as_view(), name='FeedbackList'),
    path('FeedbackCreate', views.FeedbackCreate.as_view(), name='FeedbackCreate'),
    path('TeacherDetailCreate', views.TeacherDetailCreate.as_view(),
         name='TeacherDetailCreate'),
    path('TeacherDetail', views.TeacherDetailView.as_view(),
         name='TeacherDetailView'),
    path('SchoolActivity', views.SchoolActivityList.as_view(),
         name='SchoolActivityList'),
    path('SchoolActivityCreate', views.SchoolActivityCreate.as_view(),
         name='SchoolActivityCreate'),
]
