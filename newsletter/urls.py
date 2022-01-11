from django.urls import path

from .views import NewsletterSignUpView

urlpatterns = [
    path('', NewsletterSignUpView.as_view(), name='index'),
]
