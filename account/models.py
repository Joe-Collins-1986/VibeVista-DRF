from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Account(models.Model):
    """
    Account Model:
    1:2:1 Key - User
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    image = ResizedImageField(
        default='../images/accountImages/default-account-img.jpeg',
        upload_to='images/accountImages/',
        blank=True,
        size=[150, 150],
        crop=['middle', 'center'],
        force_format='JPEG')

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner}'s account"


def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(owner=instance)


post_save.connect(create_account, sender=User)
