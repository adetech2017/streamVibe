from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('live-streams/create/', views.CreateLiveStreamView.as_view(), name='create-live-stream'),
    path('live-streams/<int:stream_id>/send-gift/', views.SendVirtualGiftView.as_view(), name='send-virtual-gift'),
    path('subscription-plans/', views.ListSubscriptionPlansView.as_view(), name='list-subscription-plans'),
    path('live-streams/', views.LiveStreamListCreateView.as_view(), name='list-create-live-stream'),
    path('live-streams/<int:stream_id>/', views.LiveStreamDetailUpdateDeleteView.as_view(), name='detail-update-delete-live-stream'),
    path('live-streams/<int:stream_id>/add-comment/', views.AddCommentView.as_view(), name='add-comment-to-live-stream'),
    path('live-streams/<int:stream_id>/like/', views.LikeLiveStreamView.as_view(), name='like-live-stream'),
    path('notifications/', views.ListNotificationsView.as_view(), name='list-notifications'),
    # Other URL patterns for your app's views

    path('videos/', views.VideoListCreateView.as_view(), name='video-list-create'),
    path('videos/<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
    path('videos/<int:video_id>/comments/', views.VideoCommentCreateView.as_view(), name='video-comment-create'),
    path('videos/<int:video_id>/like/', views.VideoLikeCreateView.as_view(), name='video-like-create'),

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', views.CreateUserView.as_view(), name='create-user'),
]
