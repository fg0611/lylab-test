from django.urls import path
from credits import views


urlpatterns = [
    path("", views.CreditsListCreateAPIView.as_view()),
    path("clients", views.ClientListCreateAPIView.as_view()),
    path("<int:pk>", views.CreditRetrieveUpdateDestroyAPIView.as_view()),
    path("<int:pk>/approve", views.CreditApproveAPIView.as_view()),
    path("<int:pk>/deny", views.CreditDenyAPIView.as_view())
]
