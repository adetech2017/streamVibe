from rest_framework import serializers
from .models import LiveStream, VirtualGift, SubscriptionPlan, Notification, Video, VideoComment, VideoLike, LiveStreamComment, LiveStreamLike
from django.contrib.auth import get_user_model

User = get_user_model()



class LiveStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStream
        fields = '__all__'


class VirtualGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualGift
        fields = '__all__'


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'


class LiveStreamCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStreamComment
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customize how comments are represented in the API response.
        In this example, we include the username of the comment's author.
        """
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        return representation


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class VideoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComment
        fields = '__all__'

class VideoLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLike
        fields = '__all__'


class LiveStreamLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStreamLike
        fields = ('id', 'stream', 'user', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user