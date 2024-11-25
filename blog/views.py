from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

