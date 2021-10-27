from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
# models import
from core.models import (
    SiteInformation,
    Category,
    Blog,
    VideoCategory,
    VideoList,
    Videos,
    BlogComment,
)
# serializers import
from core.clientapi.serializers import (
    SiteInformationSerializer,
    CategorySerializer,
    BlogSerializer,
    BlogCommentSerializer,
    ContactMessageSerializer,
    VideoCategorySerializer,
    VideoListSerializer,
    VideosSerializer,
)

# Blogs list and blog details
class BlogViewset(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'
    
    def list(self,request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True, context ={"request" : request})
        response_dict = {"error":False, "message" : "All the blog list", "data": serializer.data}
        return Response(response_dict)
    
    def retrieve(self, request, slug):
        queryset = Blog.objects.all()
        blog = get_object_or_404(queryset, slug=slug)
        blog.views += 1
        blog.save()
        serializer = BlogSerializer(blog, context={"request":request})
        serializer_data = serializer.data
        # fetch blogcomment data
        blog_comment_detail = BlogComment.objects.filter(blog=serializer_data["id"])
        blog_comment_serializer = BlogCommentSerializer(blog_comment_detail, many=True)
        serializer_data["blog_comment"] = blog_comment_serializer.data
        return Response({"error":False, "message":"Detail of blog", "data":serializer_data})
    

blog_list       = BlogViewset.as_view({"get":"list"})



# Featured blogs
class BlogFeaturedViewset(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    
    def list(self,request):
        blog = Blog.objects.filter(featured=True)[0:1]
        serializer = BlogSerializer(blog, many=True, context ={"request" : request})
        response_dict = {"error":False, "message" : "Featured blog", "data": serializer.data}
        return Response(response_dict)
    
    
    
# Blogs comment
class BlogCommentViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'
    
    def create(self, request, slug):
        try:
            queryset = Blog.objects.all()
            blog = get_object_or_404(queryset, slug=slug)
            print("Blog = ", blog)
            serializer = BlogCommentSerializer(context = {"request":request}, data=request.data)
            print("***********************************1")
            print(serializer)
            print("***********************************2")
            serializer.is_valid(raise_exception=True)
            print("***********************************3")
            serializer.save()
            response_dict = {"error":False, "message" :"Blog created successfully"}
        except:
            print("*****************something went wrong")
            response_dict = {"error":True, "message" :"Blog not created"}
        return Response(response_dict)
    
    
    
# Blog category
class CategoryViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'
    
    def list(self,request):
        # Fetch categories
        category = Category.objects.all()
        category_serializer = CategorySerializer(category, many=True, context ={"request" : request})
        serialize_data = category_serializer.data
        response_dict = {"error":False, "message" : "Category list", "data": serialize_data}
        return Response(response_dict)
    
    def retrieve(self, request, slug):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=slug)
        serializer = CategorySerializer(category, context ={"request": request})
        serializer_data = serializer.data
        # Fetch blog under that category
        blog = Blog.objects.filter(categories = serializer_data["id"])
        blog_serializer = BlogSerializer(blog, many=True)
        serializer_data["blog_serializer"] = blog_serializer.data
        response_dict = {"error":False, "message":"Blog under the caegory", "data":serializer_data}
        return Response(response_dict)
    
    
    
# Trending blogs
class TrendingBlogViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    
    def list(self,request):
        blog  = Blog.objects.order_by('-views')[0:5]
        blog_serializer = BlogSerializer(blog, many=True, context ={"request": request} )
        serialize_data = blog_serializer.data 
        response_dict = {"error":False, "message" : "Category list", "data": serialize_data}
        return Response(response_dict)
    
    
    
# Site informaiton
class ContactViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    
    def list(self,request):
        siteinfo  = SiteInformation.objects.all()
        siteinfo_serializer = SiteInformationSerializer(siteinfo, many=True, context ={"request": request} )
        serialize_data = siteinfo_serializer.data 
        response_dict = {"error":False, "message" : "Site information", "data": serialize_data}
        return Response(response_dict)
    
    
    
# Sent contact message
class ContactMessageViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    
    def create(self, request):
        try:
            serializer = ContactMessageSerializer(context = {"request":request},data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error":False, "message" :"Message sent successfully"}
        except:
            print("Soemthing went wrong with contact message")
            response_dict = {"error":True, "message" :"There is something error"}
        return Response(response_dict)
    
    
    
# VideoCategory
class VideoCategoryViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'
    
    def list(self,request):
        video_category  = VideoCategory.objects.all()
        video_category_serializer = VideoCategorySerializer(video_category, many=True, context ={"request": request} )
        serialize_data = video_category_serializer.data 
        response_dict = {"error":False, "message" : "All the videos", "data": serialize_data}
        return Response(response_dict)
    
    def retrieve(self, request, slug):
        queryset = VideoCategory.objects.all()
        category = get_object_or_404(queryset, slug=slug)
        serializer = VideoCategorySerializer(category, context ={"request": request})
        serializer_data = serializer.data
        # Fetch blog under that category
        video = VideoList.objects.filter(topic = serializer_data["id"])
        video_serializer = VideoListSerializer(video, many=True)
        serializer_data["video_serializer"] = video_serializer.data
        response_dict = {"error":False, "message":"Video under the category", "data":serializer_data}
        return Response(response_dict)
    
    
    
# VideoList and Videos
class VideoListViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'
    
    def retrieve(self, request, slug):
        queryset = VideoList.objects.all()
        category = get_object_or_404(queryset,slug=slug)
        serializer = VideoListSerializer(category, context ={"request": request})
        serializer_data = serializer.data
        # Fetch blog under that category
        video = Videos.objects.filter(videolist = serializer_data["id"])
        video_serializer = VideosSerializer(video, many=True)
        serializer_data["video_serializer"] = video_serializer.data
        response_dict = {"error":False, "message":"Single video", "data":serializer_data}
        return Response(response_dict)
    

