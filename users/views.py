import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from avito import settings
from users.models import Location, User
from users.serializers import UserSerializer, LocationSerializer, LocationCreateSerializer, UserCrateSerializer, \
    UserUpdateSerializer


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


    """def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        response = []
        for location in self.object_list:
            response.append({
                "id": location.id,
                "name": location.name,
                "lat": location.lat,
                "lng": location.lng,
            })

        return JsonResponse(response, safe=False)"""


class LocationDetailView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    """model = Location

    def get(self, request, *args, **kwargs):
        location = self.get_object()

        return JsonResponse({
            "id": location.id,
            "name": location.name,
            "lat": location.lat,
            "lng": location.lng,
        })"""


class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    """model = Location
    fields = ["name", "lat", "lng"]

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)

        location = Location.objects.create(
            name=json_data["name"],
            lat=json_data["lat"],
            lng=json_data["lng"],
        )

        return JsonResponse({
            "id": location.id,
            "name": location.name,
            "lat": location.lat,
            "lng": location.lng,
        }, status=201)"""


class LocationUpdateView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    """model = Location
    fields = ["name", "lat", "lng"]

    def put(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        json_data = json.loads(request.body)

        self.object.name = json_data["name"]
        self.object.lat = json_data["lat"]
        self.object.lng = json_data["lng"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "lat": self.object.lat,
            "lng": self.object.lng,
        })"""


class LocationDeleteView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    """model = Location
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=204)"""


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCrateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
