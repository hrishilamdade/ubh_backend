from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_json'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get-user-info/',GetUserInfo.as_view(),name="get-user-info")
]
