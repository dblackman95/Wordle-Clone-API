from rest_framework import serializers
from murmur.models import User, Relationship, Murmur, MurmurLike

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "username", "created"]

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = '__all__'

class MurmurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Murmur
        fields = '__all__'

class MurmurLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MurmurLike
        fields = '__all__'

