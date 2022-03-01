import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad
from ads.serializers import CategorySerializer, AdSerializer
from avito import settings
from users.models import User


def index(request):

    return JsonResponse({"status": "ok"})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def list(self, request):
        cat = request.GET.get("cat", None)
        text = request.GET.get("text", None)
        location = request.GET.get("location", None)
        if cat:
            self.queryset = self.queryset.filter(category=cat)
        if text:
            self.queryset = self.queryset.filter(name__contains=text)
        if location:
            self.queryset = self.queryset.filter(user__locations__name__icontains=location)

        return super().list(self, request)
