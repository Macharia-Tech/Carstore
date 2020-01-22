from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    '''
    Class that contains User Profile details
    '''
    profile_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    contact=models.CharField(max_length=25)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        '''
        Setting up self 
        '''
        return self.bio

    @classmethod
    def get_profile(cls):
        '''
        Method to retrieve the profile details
        '''
        profile=cls.objects.all()
        return profile

    def save_profile(self):
        '''
        Method to save the created profile
        '''
        self.save()

    def delete_profile(self):
        '''
        Method to delete the profile
        '''
        self.delete()

    @classmethod
    def single_profile(cls,user_id):
        '''
        function gets a single profile posted by id
        '''
        profile=cls.objects.filter(editor=user_id)
        return profile

    @classmethod
    def get_profilepic_id(cls,imageId):
        '''
        function that gets a profilepic id    
        '''
        image_id=cls.objects.filter(id=imageId)
        return image_id

class Image(models.Model):
    name=models.CharField(max_length=20)
    image_caption=models.CharField(max_length=1000,blank=True)
    image_path=models.ImageField(upload_to='images/',blank=True)
    profile=models.ForeignKey(Profile, on_delete = models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes' ,blank=True)
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def get_id(cls):
        prof=Image.objects.all()
        return prof
    @classmethod
    def get_image(cls):
        images=Profile.objects.all()
        return images
    def total_likes(self):
        return self.likes.count()
class Comment (models.Model):
    comment=models.CharField(max_length=50)
    image=models.ForeignKey(Image, on_delete = models.CASCADE)
    user=models.ForeignKey(User, on_delete = models.CASCADE)
