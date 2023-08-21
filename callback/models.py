from django.db import models


class CallbackRequest(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.phone_number
    