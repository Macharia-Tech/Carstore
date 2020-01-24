from rest_framework import serializers
from .models import Profile, Gari


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio','user')

class GariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gari
        fields = ('brand', 'image', 'description','user','profile','pub_date','price')