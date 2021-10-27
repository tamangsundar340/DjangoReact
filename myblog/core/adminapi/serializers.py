from django.db.models import fields
from rest_framework import serializers
from core.models import (
    SiteAdmin,
    Member,
    SiteInformation,
    Category,
    Blog,
    ContactMessage,
    BlogComment,
    Lesson,
    Newsletter,
    VideoCategory,
    VideoList,
    Videos
)

# SiteAdmin serialization
class SiteAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model  = SiteAdmin
        fields = "__all__"
        
        
# Member serialization
class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Member
        fields = "__all__"
        
        
# SiteInformation serialization
class SiteInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model  = SiteInformation
        fields = "__all__"
        

# Blogs serialization
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = "__all__"
        

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Blog
        fields = "__all__"
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['categories'] = CategorySerializers(instance.categories).data
        return response


class BlogCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model  = BlogComment
        fields = "__all__"
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['blog'] = BlogSerializers(instance.blog).data
        return response
        
        
        
# Lesson serialization
class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Lesson
        fields = "__all__"
    
        
# Newsletter serialization
class NewsletterSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Newsletter
        fields = "__all__"

# ContactMessage
class ContactMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model  = ContactMessage
        fields = "__all__"



# Videos
class VideoCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model  = VideoCategory
        fields = "__all__"
        
        
class VideoListSerializers(serializers.ModelSerializer):
    class Meta:
        model  = VideoList
        fields = "__all__"
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['topic'] = VideoCategorySerializers(instance.topic).data
        return response
        
        
class VideosSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Videos
        fields = "__all__"
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['videolist'] = VideoListSerializers(instance.videolist).data
        return response