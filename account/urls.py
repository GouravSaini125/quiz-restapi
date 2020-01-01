from django.urls import include, path
from . import views

urlpatterns = [
    # path("login", views.login, name="login"),
    # path('', views.UserListView.as_view(), name="UserList"),
    path('student/create', views.StudentCreateView.as_view(), name="StudentCreate"),
    path('bloodbank/create', views.BloodBankCreateView.as_view(),
         name="BloodBankCreate"),
    path('rest-auth/', include('rest_auth.urls')),
]
