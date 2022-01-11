from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(max_length = 64)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):  
        return reverse("index")

    def __str__(self):
        return self.email
