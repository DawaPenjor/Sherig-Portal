from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile,CustomUser

from django.conf import settings

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.username,
            email=user.email,
            school = user.school,
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.username = profile.name
        user.email = profile.email
        user.school = profile.school
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=CustomUser)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
