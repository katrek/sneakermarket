from django.urls import path
from .views import SneakersView, SneakerDetailView, SneakerCreateView


urlpatterns = [
    path('', SneakersView.as_view(), name='sneakers'),
    path('details/<int:pk>/', SneakerDetailView.as_view(), name='sneaker-details'),
    path('add/', SneakerCreateView.as_view(), name='add-sneakers'),
]