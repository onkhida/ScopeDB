from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# instead of modifying the built in django User model, i like to make a seperate profile to extend that

class Profile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profiles')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}'s Profile".format(self.user.username)
