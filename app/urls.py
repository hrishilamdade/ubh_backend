from django.urls import path
from .views import *

urlpatterns = [
    path('empanelments/<int:id>', EmpanelmentView.as_view(), name='empanelments'),
    path('empanelments/', EmpanelmentView.as_view(), name='empanelments'),
]
