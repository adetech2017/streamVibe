from rest_framework import status
from django.conf import settings
#from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import LiveStream, VirtualGift, SubscriptionPlan, LiveStreamLike, Notification, Video, VideoComment, VideoLike
from rest_framework import generics
from .serializers import (
    LiveStreamSerializer,
    VirtualGiftSerializer,
    SubscriptionPlanSerializer,
    LiveStreamCommentSerializer,
    NotificationSerializer,
    VideoSerializer,
    VideoCommentSerializer,
    VideoLikeSerializer,
    LiveStreamLikeSerializer,
    UserSerializer
)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        # Use the custom user model from settings.AUTH_USER_MODEL
        return settings.AUTH_USER_MODEL.objects.all()


class CreateLiveStreamView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveStreamSerializer


class SendVirtualGiftView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VirtualGiftSerializer

    def perform_create(self, serializer):
        stream_id = self.kwargs['stream_id']
        stream = generics.get_object_or_404(LiveStream, pk=stream_id)
        serializer.save(sender=self.request.user, stream=stream)


class ListSubscriptionPlansView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionPlanSerializer
    queryset = SubscriptionPlan.objects.all()


class LiveStreamListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveStreamSerializer
    queryset = LiveStream.objects.filter(is_live=True)

    def perform_create(self, serializer):
        serializer.save(streamer=self.request.user)


class LiveStreamDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveStreamSerializer
    queryset = LiveStream.objects.all()
    lookup_field = 'pk'


class AddCommentView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveStreamCommentSerializer

    def perform_create(self, serializer):
        stream_id = self.kwargs['stream_id']
        stream = generics.get_object_or_404(LiveStream, pk=stream_id)
        serializer.save(stream=stream, user=self.request.user)


class LikeLiveStreamView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveStreamLikeSerializer

    def perform_create(self, serializer):
        stream_id = self.kwargs['stream_id']
        stream = generics.get_object_or_404(LiveStream, pk=stream_id)
        serializer.save(stream=stream, user=self.request.user)


class ListNotificationsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')


# Example: Trigger notification for a live stream start
def notify_followers_on_live_stream_start(streamer):
    followers = streamer.profile.followers.all()  # Assuming you have a 'followers' relation
    message = f"{streamer.username} started a live stream: {streamer.title}"
    for follower in followers:
        Notification.objects.create(recipient=follower, sender=streamer, message=message, notification_type='live_stream_start')


class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    #permission_classes = [IsAuthenticated]


class VideoCommentCreateView(generics.CreateAPIView):
    serializer_class = VideoCommentSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        video_id = self.kwargs['video_id']
        serializer.save(user=self.request.user, video_id=video_id)


class VideoLikeCreateView(generics.CreateAPIView):
    serializer_class = VideoLikeSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        video_id = self.kwargs['video_id']
        serializer.save(user=self.request.user, video_id=video_id)