from rest_framework import serializers
from .models import Profile, Gari


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio','user')

class GariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'image', 'description','user','profile','pub_date','price')