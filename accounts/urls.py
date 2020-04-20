from django.urls import path, include
from .views import (SignUpView,
                    LogInView,
                    LogOutView,
                    UserData,)

app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('user_info/', UserData.as_view(), name="User"),
    path('oauth', include('rest_framework_social_oauth2.urls'))
]
