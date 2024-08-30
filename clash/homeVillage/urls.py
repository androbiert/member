from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path("profile",views.profile,name="profile"),
    path("delete/<str:id>",views.delete_member,name='delete_profile'),
]

