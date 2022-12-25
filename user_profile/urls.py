from django.urls import path
from . import views as vs


urlpatterns = [
    # path('', vs.to_user_profile_page, name='touserprofilepage'),
    path('', vs.user_profile_page, name='userprofilepage'),
    path('login/', vs.LoginPage.as_view(), name='loginpage'),
    path('logout/', vs.logout_page, name='logoutpage')
]