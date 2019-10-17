from django.urls import path
from .views import SignUpView, UserProfileView, UserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('profile/edit/<int:pk>/', UserUpdateView.as_view(), name='profile-edit'),

]

