from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register_view,name="register"),
    path('login/',views.login_view,name="login"),
    path('profile/',views.profile_view,name="profile"),
    path('logout/',views.logout_view,name="logout"),
    path('profile/change_password/',views.change_password,name="change_password"),
    path('reset_password/',views.reset_password,name="reset_password"),
    path('success/',views.success_page,name="success"),
    path('error',views.error_page,name="error")
]