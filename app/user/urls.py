"""
URL mapping for the user api
"""
from django.urls import path

from user import views

# this allows test_user_api (reverse mapping) to find the app 'user'
app_name = 'user'

# this allows test_user_api (reverse mapping) to find the function 'create'
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
