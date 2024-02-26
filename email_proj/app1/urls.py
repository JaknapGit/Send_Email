from django.urls import path
from .views import AccountView

urlpatterns = [
    path('emails/', AccountView.as_view(), name='emails')
]