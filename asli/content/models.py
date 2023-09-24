from django.db import models
from accounts.models import User
# Create your models here.

def get_twit_image_filepath(self , filename):
    return 'img_twit/images/' + str(self.pk) + 'profile_image.png'

class Twit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_twit')
    img = models.ImageField(upload_to=get_twit_image_filepath , null=True , blank=True)
    description = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username

# Comments Twit Model
class CommentTwit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
    twit = models.ForeignKey(Twit,on_delete=models.CASCADE,related_name='twit_user')
    sub = models.ForeignKey('self',on_delete=models.CASCADE,related_name='sub_user',null=True , blank=True)
    is_sub = models.BooleanField(default=False)
    comment = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username} Commented {self.twit}'
    
# Like Twit Model
class Relation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='like_user')
    twit = models.ForeignKey(Twit,on_delete=models.CASCADE,related_name='twit_like')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username} Liked Twits {self.twit}'
    
# Save Twit Model
class SaveTwit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='save_user')
    twit = models.ForeignKey(Twit,on_delete=models.CASCADE,related_name='twit_save')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} Save Twit {self.twit}'

