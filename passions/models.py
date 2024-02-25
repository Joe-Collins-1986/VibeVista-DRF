from django.db import models
from django.contrib.auth.models import User
from partner_profile.models import PartnerProfile


class Passion(models.Model):
    """
    Passion Model:
    Foreign Key - User & PartnerProfile
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_profile = models.ForeignKey(PartnerProfile, on_delete=models.CASCADE, related_name='passions')
    passion_text = models.CharField(max_length=255) 
    

    def __str__(self):
        return f"{self.partner_profile}'s passion: {self.passion_text}"