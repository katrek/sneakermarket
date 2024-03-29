from django.urls import path
from .views import SignUpView, UserUpdateView, UserListView, SingleUserView, UserProfile

urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', SingleUserView.as_view(), name='single-user-profile'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='user-profile'),
    path('profile/edit/', UserUpdateView.as_view(), name='profile-edit'),
]

