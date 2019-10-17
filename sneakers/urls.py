from django.urls import path
from .views import SneakersView, SneakerDetailView, SneakerCreateView, SneakerDeleteView, SneakerUpdateView


urlpatterns = [
    path('', SneakersView.as_view(), name='sneakers'),
    path('details/<int:pk>/', SneakerDetailView.as_view(), name='sneaker-details'),
    path('add/', SneakerCreateView.as_view(), name='add-sneakers'),
    path('delete/<int:pk>/', SneakerDeleteView.as_view(), name='delete-sneakers'),
    path('edit/<int:pk>/', SneakerUpdateView.as_view(), name='sneaker-edit'),
]