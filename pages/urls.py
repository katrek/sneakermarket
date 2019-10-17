from django.urls import path
from .views import HomepageView, AboutPage

urlpatterns = [
    path('', HomepageView.as_view(), name='index'),
    path('about/', AboutPage.as_view(), name='about'),
]