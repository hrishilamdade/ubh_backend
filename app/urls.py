from django.urls import path
from .views import *

urlpatterns = [
    path('empanelments/<int:id>', EmpanelmentView.as_view(), name='empanelments'),
    path('empanelments/', EmpanelmentView.as_view(), name='empanelments'),
    path('meta-experts/<int:id>', MetaExpertView.as_view(), name='meta-experts'),
    path('meta-experts/', MetaExpertView.as_view(), name='meta-experts'),
    path('empanelment-to-meta-experts/', EmpanelmentToMetaView.as_view(), name='empanelment-to-meta-experts'),
]
