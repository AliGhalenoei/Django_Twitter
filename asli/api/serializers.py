from rest_framework import serializers
from accounts.models import *
from content.models import *


# Serializers App Content...

class TwitSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Twit
        fields =('__all__')

    # def create(self, validated_data):
    #     return Twit.objects.create(**validated_data)

class CommentTwitSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    twit = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = CommentTwit
        fields = ('__all__')

class RelationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    twit = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Relation
        fields =('__all__')

class SaveTwitSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    twit = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = SaveTwit
        fields =('__all__')

# Serializers App Accounts...

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserSinginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate_email(self , value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError('Email Is alredy')
        return value
    
    def validate_username(self , value):
        if User.objects.filter(username = value).exists():
            raise serializers.ValidationError('Username Is alredy')
        return value
    
    def validate(self, value):
        if value['password'] and value['password2'] and value['password'] != value['password2']:
            raise serializers.ValidationError('Passwords is Not Match')
        return value
    
class UserFollw_UnFollwSerializer(serializers.ModelSerializer):
    user_follw = serializers.StringRelatedField(read_only = True)
    user_follwing = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = UserFollw_UnFollw
        fields =('__all__')







    
