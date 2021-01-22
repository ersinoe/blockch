from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name="users-register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="users-logout"),
    path("profile/", views.profile, name="users-profile"),
    path("notes/", views.notes, name="users-notes"),
    path('protect/<id>', views.protect, name="users-protect"),
    path('checkprotection/', views.checkprotection, name="users-checkprotection"),
    path("authenticate/", views.authenticate, name="users-authenticate")
]