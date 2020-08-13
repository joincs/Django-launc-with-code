from django.db import models
from django.urls import reverse

# Create your models here.

class Join(models.Model):
    email      = models.EmailField()
    firend     = models.ForeignKey("self",related_name='referral',null=True,blank=True,on_delete=models.SET_NULL)
    ref_id     = models.CharField(max_length=120, null=True)
    ip_address = models.CharField(max_length=120,null=True)
    timestamp  = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("first_app:share",kwargs={'ref_id':self.ref_id})