from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    # ListAPIView,
    # CreateAPIView,
    # UpdateAPIView,
    # RetrieveAPIView,
    # DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
# models import
from core.models import (
    SiteAdmin,
    Member,
    SiteInformation,
    Category,
    Blog,
    BlogComment,
    Lesson,
    Newsletter,
    ContactMessage,
    VideoCategory,
    VideoList,
    Videos
)
# import serilizers class
from .serializers import *


# SiteAdmin
class SiteAdminListCreateView(ListCreateAPIView):
    queryset           = SiteAdmin.objects.all()
    serializer_class   = SiteAdminSerializers

class SiteAdminUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = SiteAdmin.objects.all()
    serializer_class   = SiteAdminSerializers
    
    
# Member
class MemberListCreateView(ListCreateAPIView):
    queryset           = Member.objects.all()
    serializer_class   = MemberSerializers

class MemberUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = Member.objects.all()
    serializer_class   = MemberSerializers
    

# SiteInformation
class SiteInformationListCreateView(ListCreateAPIView):
    queryset           = SiteInformation.objects.all()
    serializer_class   = SiteInformationSerializers

class SiteInformationUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = SiteInformation.objects.all()
    serializer_class   = SiteInformationSerializers
    
    
# Category
class CategoryListCreateView(ListCreateAPIView):
    queryset           = Category.objects.all()
    serializer_class   = CategorySerializers

class CategoryUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = Category.objects.all()
    serializer_class   = CategorySerializers
    
    
# Blog
class BlogListCreateView(ListCreateAPIView):
    queryset           = Blog.objects.all()
    serializer_class   = BlogSerializers

class BlogUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = Blog.objects.all()
    serializer_class   = BlogSerializers
    
    
# BlogComment
class BlogCommentListCreateView(ListCreateAPIView):
    queryset           = BlogComment.objects.all()
    serializer_class   = BlogCommentSerializers

class BlogCommentUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = BlogComment.objects.all()
    serializer_class   = BlogCommentSerializers


# Lesson
class LessonListCreateView(ListCreateAPIView):
    queryset           = Lesson.objects.all()
    serializer_class   = LessonSerializers

class LessonUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = Lesson.objects.all()
    serializer_class   = LessonSerializers
    

# Newsletter
class NewsletterListCreateView(ListCreateAPIView):
    queryset           = Newsletter.objects.all()
    serializer_class   = NewsletterSerializers

class NewsletterUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = Newsletter.objects.all()
    serializer_class   = NewsletterSerializers
    
    
    
# ContactMessage
class ContactMessageListCreateView(ListCreateAPIView):
    queryset           = ContactMessage.objects.all()
    serializer_class   = ContactMessageSerializers
    
class ContactMessageUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = ContactMessage.objects.all()
    serializer_class   = ContactMessageSerializers
    
    
#Video
class VideoCategoryListCreateView(ListCreateAPIView):
    queryset           = VideoCategory.objects.all()
    serializer_class   = VideoCategorySerializers

class VideoCategoryUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = VideoCategory.objects.all()
    serializer_class   = VideoCategorySerializers
    
    
class VideoListCreateView(ListCreateAPIView):
    queryset           = VideoList.objects.all()
    serializer_class   = VideoListSerializers

class VideoListUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = VideoList.objects.all()
    serializer_class   = VideoListSerializers
    

class VideosListCreateView(ListCreateAPIView):
    queryset           = Videos.objects.all()
    serializer_class   = VideosSerializers

class VideosUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_filed       = 'pk'
    queryset           = Videos.objects.all()
    serializer_class   = VideosSerializers