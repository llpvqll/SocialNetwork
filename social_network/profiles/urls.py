from django.urls import path
from . import views

urlpatterns = [
    path('', views.List.as_view()),
    # path('<slug>', ProfileDetailView.as_view()),
]