from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('create', views.UserCreateView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]