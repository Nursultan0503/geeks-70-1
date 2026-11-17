from django.urls import path
from users.views import RegisterView, AuthLoginView, AuthLogoutView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='reg'),
    path('login/', AuthLoginView.as_view(), name='log'),
    path('logout/', AuthLogoutView.as_view(), name='lgout'),
    path('profile/', ProfileView.as_view(), name='prof'),
]
