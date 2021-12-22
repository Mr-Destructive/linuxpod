from django.urls import path

from .views import HomePageView, Update_List

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('update/', Update_List.as_view(), name="update_homepage"),
]
