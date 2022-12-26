from django.urls import path
from . import views as vs


urlpatterns = [
    path('', vs.to_user_profile_page, name='touserprofilepage'),
    path('<username>/', vs.user_profile_page, name='userprofilepage'),
    path('account/login/', vs.login_page, name='loginpage'),
    path('account/logout/', vs.logout_page, name='logoutpage')
]