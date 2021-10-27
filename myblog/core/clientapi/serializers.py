from rest_framework import serializers

from core.models import (
    SiteInformation,
    Category,
    Blog,
    BlogComment,
    VideoCategory,
    VideoList,
    Videos,
    ContactMessage
)


# SiteInformation
class SiteInformationSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = SiteInformation
        fields = '__all__'
        lookup_field = 'slug'
        
        
        
# Blogs, BlogsCategory and BlogComment
class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%m-%Y")
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'
        
        
class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%m-%Y")
    class Meta:
        model = Blog
        fields ='__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['categories'] = CategorySerializer(instance.categories).data
        return response
    
    
class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['blog'] = BlogSerializer(instance.blog).data
        return response
    
    
    
# VideoCategory, VideoList and Videos
class VideoCategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = VideoCategory
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        
        
class VideoListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = VideoList
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['topic'] = VideoCategorySerializer(instance.topic).data
        return response
    
    
class VideosSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = Videos
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['videolist'] = VideoListSerializer(instance.videolist).data
        return response
    
    
    
# ContactMessage
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        lookup_field = 'slug'
