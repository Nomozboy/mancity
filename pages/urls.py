from django.urls import path
from .views import HomePageView, SquadPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('squad/', SquadPageView.as_view(), name='squad'),
]
