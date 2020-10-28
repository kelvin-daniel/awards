from rest_framework import serializers
from .models import Projects,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=('sitename','url','description','location','date')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('profile','bio','user')