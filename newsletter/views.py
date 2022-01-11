from django.shortcuts import render
from django.views.generic import CreateView
from .models import Newsletter
from .forms import NewsletterSignupForm

class NewsletterSignUpView(CreateView):
    model = Newsletter
    form_class = NewsletterSignupForm
    template_name = 'newsletter/signup.html'

    def form_valid(self, form):
        return super(NewsletterSignUpView, self).form_valid(form)
