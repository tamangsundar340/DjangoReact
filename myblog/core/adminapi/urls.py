from django.urls import path

from .views import(
    # SiteAdmin
    SiteAdminListCreateView,
    SiteAdminUpdateDestroyView,
    # Member
    MemberListCreateView,
    MemberUpdateDestroyView,
    # SiteInformation
    SiteInformationListCreateView,
    SiteInformationUpdateDestroyView,
    # Category
    CategoryListCreateView,
    CategoryUpdateDestroyView,
    #Blog 
    BlogListCreateView,
    BlogUpdateDestroyView,
    #BlogComment
    BlogCommentListCreateView,
    BlogCommentUpdateDestroyView,
    # Lesson
    LessonListCreateView,
    LessonUpdateDestroyView,
    # Newsletter
    NewsletterListCreateView,
    NewsletterUpdateDestroyView,
    # ContactMessage
    ContactMessageListCreateView,
    ContactMessageUpdateDestroyView,
    # VideoCategory
    VideoCategoryListCreateView,
    VideoCategoryUpdateDestroyView,
    # VideoList
    VideoListCreateView,
    VideoListUpdateDestroyView,
    # Videos
    VideosListCreateView,
    VideosUpdateDestroyView
    
)


urlpatterns = [    
    # SiteAdmin
    path('siteadmin-createlist', SiteAdminListCreateView.as_view(), name='siteadmin-createlist'),
    path('siteadmin-destroyupdate/<str:pk>/', SiteAdminUpdateDestroyView.as_view(), name='siteadmin-destroyupdate'),
    # Member
    path('member-createlist', MemberListCreateView.as_view(), name='member-createlist'),
    path('member-destroyupdate/<str:pk>/', MemberUpdateDestroyView.as_view(), name='member-destroyupdate'),
    # SiteInformation
    path('siteinfo-createlist', SiteInformationListCreateView.as_view(), name='siteinfo-createlist'),
    path('siteinfo-destroyupdate/<str:pk>/', SiteInformationUpdateDestroyView.as_view(), name='siteinfo-destroyupdate'),
    # Category
    path('category-createlist', CategoryListCreateView.as_view(), name='category-createlist'),
    path('category-destroyupdate/<str:pk>/', CategoryUpdateDestroyView.as_view(), name='category-destroyupdate'),
    # Blog 
    path('blog-createlist', BlogListCreateView.as_view(), name='blog-createlist'),
    path('blog-destroyupdate/<str:pk>/', BlogUpdateDestroyView.as_view(), name='blog-destroyupdate'),
    # BlogComment
    path('blogcomment-createlist', BlogCommentListCreateView.as_view(), name='blogcomment-createlist'),
    path('blogcomment-destroyupdate/<str:pk>/', BlogCommentUpdateDestroyView.as_view(), name='blogcomment-destroyupdate'),
    # Lesson
    path('lesson-createlist', LessonListCreateView.as_view(), name='lesson-createlist'),
    path('lesson-destroyupdate/<str:pk>/', LessonUpdateDestroyView.as_view(), name='lesson-destroyupdate'),
    # Newsletter
    path('newsletter-createlist', NewsletterListCreateView.as_view(), name='newsletter-createlist'),
    path('newsletter-destroyupdate/<str:pk>/', NewsletterUpdateDestroyView.as_view(), name='newsletter-destroyupdate'),
    # Contact message
    path('contact-message', ContactMessageListCreateView.as_view(), name='contact-message'),
    path('contactmessage-destroyupdate/<str:pk>/', ContactMessageUpdateDestroyView.as_view(), name='contactmessage-destroyupdate'),
    # VideoCategory
    path('videocategory-createlist', VideoCategoryListCreateView.as_view(), name='videocategory-createlist'),
    path('videocategory-destroyupdate/<str:pk>/', VideoCategoryUpdateDestroyView.as_view(), name='videocategory-destroyupdate'),
    # VideoList
    path('videolist-createlist', VideoListCreateView.as_view(), name='videolist-createlist'),
    path('videolist-destroyupdate/<str:pk>/', VideoListUpdateDestroyView.as_view(), name='videolist-destroyupdate'),
    # Videos
    path('video-createlist', VideosListCreateView.as_view(), name='video-createlist'),
    path('video-destroyupdate/<str:pk>/', VideosUpdateDestroyView.as_view(), name='video-destroyupdate'),
]