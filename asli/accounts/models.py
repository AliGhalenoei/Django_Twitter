from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from .managers import UserManager
# Create your models here.

def get_profile_image_filepath(self , filename):
    return 'profile/profile_images/' + str(self.pk) + 'profile_image.png'

def get_default_profile_image():
    return 'profile/profile_default/default_profile_image.png'

class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    img = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    bio = models.TextField(null=True , blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
class UserFollw_UnFollw(models.Model):
    user_follw = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_follw')
    user_follwing = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_follwing')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user_follw.username} Follwing.... {self.user_follwing.username}'
    