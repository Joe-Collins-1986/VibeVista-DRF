from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from likes.models import Like
from characteristics.models import Characteristic


class PartnerProfile(models.Model):
    """
    UserProfile Model:
    Foreign Key - User
    """
    primary_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    about = models.TextField(blank=True)
    image = ResizedImageField(
        default='../images/partnerImages/default-partner-img.jpeg',
        upload_to='images/partnerImages/',
        blank=True,
        size=[150, 150],
        crop=['middle', 'center'],
        force_format='JPEG')
    characteristics = models.ManyToManyField(Characteristic, related_name='partner_profiles', blank=True)
    likes = models.ManyToManyField(Like, related_name='partner_profiles', blank=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.primary_profile}'s partner profile: {self.name}"