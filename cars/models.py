from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    Bio= models.TextField()
    profile_image=models.ImageField(upload_to = 'profiles/',blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    @classmethod
    def search(cls,search_term):
        profiles=cls.objects.filter(user__id__icontains=search_term)
        return profiles
        
    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all()
        return profile
    def total_following(self):
        return self.follow.count()
class Image(models.Model):
    name=models.CharField(max_length=20)
    image_caption=models.CharField(max_length=1000,blank=True)
    image_path=models.ImageField(upload_to='images/',blank=True)
    profile=models.ForeignKey(Profile, on_delete = models.CASCADE)
    
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
 
class Comment (models.Model):
    comment=models.CharField(max_length=50)
    image=models.ForeignKey(Image, on_delete = models.CASCADE)
    user=models.ForeignKey(User, on_delete = models.CASCADE)

class Gari(models.Model):
    brand=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    image=models.ImageField(upload_to = 'images/', blank=True)
    description=models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.CharField(max_length=255)


    def __str__(self):
        '''
        Setting up self
        '''
        return self.brand

    def save_gari(self):
        '''
        Method for saving the gari
        '''
        self.save()

    
    def delete_gari(self):
        '''
        Method for deleting the gari
        '''
        self.delete()

    @classmethod
    def get_garis(cls):
        '''
        Method for retrieving all images
        '''
        gari=cls.objects.all()
        return gari


    @classmethod
    def user_garis(cls,user_id):
        '''
        function gets garis posted by id
        '''
        gari_posted=cls.objects.filter(user=user_id)
        return gari_posted    


    @classmethod
    def search_by_brand(cls,tag):
        '''
        Method for searching for a gari using the title
        '''

        search_result=cls.objects.filter(brand__icontains=tag)
        return search_result

    @classmethod
    def single_gari(cls,gari_id):
        '''
        function gets a single gari posted by id
        '''
        gari_posted=cls.objects.get(id=gari_id)
        return gari_posted

    @classmethod
    def get_image_id(cls,imageId):
        '''
        function that gets an image id    
        '''
        image_id=cls.objects.filter(id=imageId)
        return image_id